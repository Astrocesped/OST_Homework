#
# 2015 July 20th
#
""" Tests email_parser.py. """

import unittest
import email_parser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Test_EmailParser(unittest.TestCase):
    
    def setUp(self):
        self.email_address = "info@carlosmontesr.com"
    
    def test_email_parser(self):
        
        text_file = "test.txt"
        html_file = "test.html"
        image_file = "test.png"
        
        # Create an MIME-type email object, attach address and files
        message = MIMEMultipart()
        message["to"] = self.email_address
        
        # Load a text file
        with open(text_file, "r") as t:
            message.attach(MIMEText(t.read(), "plain"))
        
        # Load HTML file
        with open(html_file, "r") as h:
            message.attach(MIMEText(h.read(), "html"))
        
        # Load an image file
        with open(image_file, "rb") as i:
            message.attach(MIMEImage(i.read()))
        
        test_message = email_parser.create_file_message(self.email_address,
                                                        text_file,
                                                         html_file,
                                                         image_file)
        
        self.assertEqual(test_message["to"], message["to"])
        
        # Boundary strings will always be randomly generated, right? Skip this
        #self.assertEqual(test_message.as_string(), message.as_string())
        
        # Test same content type
        content_list = [m.get_content_type() for m in message.walk()]
        for i, section in enumerate(test_message.walk()):
            self.assertEqual(section.get_content_type(), content_list[i])
        
    def test_unattachable_files(self):
        
        bin_file = "test.bin"
        
        # Create an MIME-type email object, don't attach bin_file
        message = MIMEMultipart()
        message["to"] = self.email_address
        
        test_message = email_parser.create_file_message(self.email_address,
                                                        bin_file)
        
        self.assertEqual(len(test_message.as_string()),
                         len(message.as_string()))
        
        
if __name__ == "__main__":
    unittest.main()
