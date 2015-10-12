"""
Unittest module for email_scheduler.py
"""

import unittest
import datetime
import time
import settings
import email_scheduler

TABLE_NAME = "carlos_emails"

class testEmailScheduler(unittest.TestCase):
    
    def test_message_creation(self):
        """
        Test the email message object creation function.
        """
        sender = "test@test.com"
        
        msg = email_scheduler.create_message(settings.STARTTIME,
                                             sender,
                                             settings.RECIPIENTS[0],
                                             "Test Message")
        
        self.assertEqual(msg["Date"], settings.STARTTIME)
        self.assertEqual(msg["From"], '<a href="{0}">{0}</a>'.format(sender))
        self.assertEqual(msg["To"], settings.RECIPIENTS[0][1])
        self.assertEqual(msg["Message-Id"], "<NNNNN>")
        self.assertEqual(msg.get_payload(), "Test Message")
    
    def test_normal_performance(self):
        """
        Test email_scheduler on its normal performance, taking default
        parameters from settings.py and entering them in the database
        with day intervals.
        """
        # Create an instance of a Message_Scheduler, which will
        # store data on a temporary table, to be deleted afterwards
        test_scheduler = email_scheduler.Message_Scheduler(TABLE_NAME)
        
        from_addr = 'info@carlosmontesr.com'
        
        test_scheduler.insert_messages(from_addr, "Test body")
        
        with email_scheduler.DB_Connection() as conn:
            curs = conn.cursor()
            
            # Test the settings' RECIPIENTS length multiplied by the
            # DAYCOUNT to be equal to the number of generated email messages
            # stored in the database
            curs.execute("SELECT COUNT(*) FROM {0}".format(TABLE_NAME))
            messagecount = curs.fetchone()[0]
            self.assertEqual(messagecount,
                             settings.DAYCOUNT * len(settings.RECIPIENTS))
        
            # Delete the created table
            curs.execute("DROP TABLE IF EXISTS {0}".format(TABLE_NAME))
            conn.commit()
            
    def test_message_insertion(self):
        """
        Tests message insertion into the database by measuring the time it
        takes for the insert_messages method to process each set of emails
        (each composed of messages to be sent to settings.RECIPIENTS on a
        shared date).
        """
        test_scheduler = email_scheduler.Message_Scheduler(TABLE_NAME)
        from_addr = 'info@carlosmontesr.com'
        
        # Measure the time it takes for the method to complete
        start_time = time.time()
        
        # Enter the first set of messages with start_time as their date
        test_scheduler.insert_messages(from_addr, "Test body 1",
                    start_time=datetime.datetime.fromtimestamp(
                    start_time).strftime("%d %b %Y %H:%M:%S -0600"),
                    total_times=1)
        end_time = time.time()
        
        # The process time is the new interval; convert it into milliseconds
        custom_interval = int((end_time - start_time) / 1000)
        
        with email_scheduler.DB_Connection() as conn:
            curs = conn.cursor()
            
            # Check the content of the first inserted row
            curs.execute("SELECT * FROM {0} WHERE id=1".format(TABLE_NAME))
            
            # Assert the value of each column (message_id , date,
            # sender_address, recip_address, body)
            first_row = curs.fetchone()
            
            self.assertEqual(first_row[1], "<NNNNN>")
            self.assertEqual(first_row[2].day,
                             datetime.datetime.fromtimestamp(start_time).day)
            self.assertEqual(first_row[2].minute,
                             datetime.datetime.fromtimestamp(start_time).minute)
            self.assertEqual(first_row[3],
                             "<a href=\"{0}\">{0}</a>".format(from_addr))
            self.assertEqual(first_row[4], settings.RECIPIENTS[0][1])
            self.assertEqual(first_row[5], "Test body 1")
            
            # Now insert the rest of the sets with the new interval; verify
            #the number of rows inserted through each iteration
            current_rows = len(settings.RECIPIENTS)
            
            for i in range(settings.DAYCOUNT - 1):
                test_scheduler.insert_messages(from_addr,
                "Test body {0}".format(i),
                start_time=datetime.datetime.fromtimestamp(
                start_time).strftime("%d %b %Y %H:%M:%S -0600"),
                total_times=1,
                interval=datetime.timedelta(days=custom_interval))
                
                # One more test verifying the current number of rows
                curs.execute("SELECT COUNT(*) FROM {0}".format(TABLE_NAME))
                messagecount = curs.fetchone()[0]
                self.assertEqual(messagecount,
                                 current_rows + ((i + 1) * current_rows))
                
            # Delete the created table
            curs.execute("DROP TABLE IF EXISTS {0}".format(TABLE_NAME))
            conn.commit()

        
if __name__ == "__main__":
    
    unittest.main()
