#!/usr/local/bin/python3
#
# Email Generator By Schedule
# email_scheduler.py
#
# 2015 July 29th
#
"""
Sends emails on an automatic timer, based on names found in settings.py
"""

import mysql.connector as mysqlc
from database import login_info
import settings
import email
import datetime
from time import strptime, mktime

def create_message(date, sender, recipient, payload):
    """
    Creates an email message with the parameters' values as its
    headers and content. Message-ID is '<NNNNNN>' for each by default.
    :param date: The message's date
    :param sender: The sender's email address
    :param recipient: Tuple containing a recipient's name and email address
    :param payload: Email's body
    :return: email message object
    """
    msg = """\
Date: {0}
From: <a href=\"{1}\">{1}</a>
To: {2}
Message-ID: <NNNNN>

{3}""".format(date, sender, recipient[1], payload)

    return email.message_from_string(msg)

class DB_Connection:
    def __enter__(self):
        """
        Connects to the database defined in database.py
        """
        self.conn = mysqlc.Connect(**login_info)
        return self.conn
        
    def __exit__(self, exception_type, exc_value, exc_tb):
        """
        Closes the connection when the context manager exits.
        """
        self.conn.close()

class Message_Scheduler:
    """
    Creates email messages, aimed to be sent to a list of recipients for
    a scheduled number of days, and stores them in a database.
    """
    def __init__(self, table_name="messages"):
        """
        Verifies table_name exists in the
        database; if not, it creates it.
        :param table_name: Name of a table where to store the email messages
        """
        self.table_name = table_name
        
        # Test that the table exists by trying to make a simple query
        with DB_Connection() as conn:
            curs = conn.cursor()
            
            try:
                curs.execute("SELECT COUNT(*) FROM {0}".format(table_name))
        
        # Create the messages table if not:
            except mysqlc.errors.ProgrammingError:
                curs.execute("""\
CREATE TABLE {0} (
     id INTEGER AUTO_INCREMENT PRIMARY KEY,
     message_id VARCHAR(128),
     date DATETIME,
     sender_address VARCHAR(128),
     recip_address VARCHAR(128),
     body LONGTEXT
) ENGINE = MYISAM""".format(self.table_name))
                conn.commit()
            
    def insert_messages(self, sender_address, payload,
                        start_time=settings.STARTTIME,
                        total_times=settings.DAYCOUNT,
                        recipient_list=settings.RECIPIENTS,
                        interval=datetime.timedelta(days=1)):
        """
        Creates email messages, and inserts each set of messages with unique
        recipient addresses for each day from start_time until the last day,
        result from adding total_times units of time to starttime.
        Certain parameter values will be imported from settings by default.
        
        :param sender_address: Email address from the sender
        :param payload: Body to be inserted in each message
        :param start_time: datetime object telling when the scheduling starts
        :param total_times: Integer detailing how many intervals will each set
        of messages with unique recipient addresses will be sent
        :param recipient_list: List with each recipient's email address
        :param interval: datetime.timedelta that will increase each set's date
        """
        # current_date holds start_time at first (after converting its
        # time_struct format to a datetime), then a new interval is added
        # in every iteration step through total_times
        current_date = datetime.datetime.fromtimestamp(
                        mktime(strptime(start_time,
                                        "%d %b %Y %H:%M:%S -0600")))
        
        for i in range(total_times):
            # List of messages with this current_time
            currentday_msglist = []
            
            # Create a list of messages on this particular day
            for recipient_address in recipient_list:
                        
                currentday_msglist.append(create_message(current_date,
                                                         sender_address,
                                                         recipient_address,
                                                         payload))
            
            # Create a row for every recipient in this unique day
            self.messages_to_database(currentday_msglist)
            
            # Modify the date by adding one more interval
            current_date += interval
    
    def messages_to_database(self, msg_list):
        """
        Enters a set of email messages with unique 'to' addresses into the
        'messages' table, with each of their individual attributes in its
        respective columns.
        :param msg_list: List of email messages to be entered into 'messages'
        """
        with DB_Connection() as conn:
            curs = conn.cursor()
            
            for msg in msg_list:
                curs.execute("""INSERT INTO {0}
                (message_id, date, sender_address, recip_address, body)
                VALUES (%s, %s, %s, %s, %s)""".format(self.table_name),
                (msg["message-id"], msg["date"],
                 msg["from"], msg["to"], msg.get_payload()))
                
                conn.commit()
    
if __name__ == "__main__":
    """
    Profiling information.
    """
    import time
    table_name = "Profiling_Test"
    from_addr = 'info@carlosmontesr.com'
    
    # Measure time to create the Profiling_Test table
    start = time.time()
    scheduler = Message_Scheduler(table_name)
    end = time.time()
    print("Time required to create the table:", end - start)
    
    def profile_time(times):
        """
        Helper function to profile insert_messages.
        :param times: Integer telling how many sets of messages to insert
        """
        start = time.time()
        scheduler.insert_messages(from_addr, "DAYCOUNT {0}".format(times),
                                  total_times=times)
        end = time.time()
        
        return end - start
    
    # Profile insert_messages for DAYCOUNT = 1
    avg_time = profile_time(1)
    print("\nAverage time for DAYCOUNT 1:", avg_time, "\n")
    
    def print_times(times):
        """
        Helper that prints to console expected and real times of using
        insert_messages with distinct argument values.
        :param times: Value of DAYCOUNT to pass
        """
        print("Expected time for DAYCOUNT {0} is:".format(times),
              avg_time * times)
        print("Real time for DAYCOUNT {0} is:".format(times),
              profile_time(times), "\n")
    
    # Print times for several DAYCOUNT values
    print_times(10)
    print_times(50)
    print_times(100)
    print_times(500)
    
    # Delete table
    with DB_Connection() as conn:
        curs = conn.cursor()
        curs.execute("DROP TABLE IF EXISTS {0}".format(table_name))
        conn.commit()
