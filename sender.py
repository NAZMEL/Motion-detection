import smtplib, ssl, os
import getpass
from csv_work import read_as_dict
from config import *
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#class for sender lists
class Sender:
    def __init__(self, receivers):
        # Create a secure SSL context
        self.context = ssl.create_default_context()
        self.sender_mail = SENDER_EMAIL
        self.sender_password = SENDER_PASSWORD
        self.message = MIMEMultipart()
        self.message['Subject'] = "MOVE DETECTED"
        self.receivers = receivers
    

    def send_mails(self,  message = MESSAGE, image='D:\Projects\Motion-detection\images\image.jpg'):

        self.message.attach(MIMEText(message))

        if image != '':
            img_data = open(image, 'rb').read()
            img = MIMEImage(img_data, name= os.path.basename(image))
            self.message.attach(img)

        # work server
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=self.context) as server: 
                try:
                    server.login(self.sender_mail, self.sender_password)

                    # send this letter to each user
                    for row in self.receivers:
                        server.sendmail(self.sender_mail,
                                        to_addrs = row["email"],
                                        msg = self.message.as_string().format(name = row["name"])
                                        )

                    print("Message was sent succesfully\n")

                except Exception as e:
                    print(e)
        except Exception as e:
            print(f"{bcolors.FAIL} {e}: {bcolors.ENDC}{bcolors.UNDERLINE} Maybe, connect to server is failed. Check connect to the Internet! {bcolors.ENDC}")
                
            

if __name__ == '__main__':

    Sender().send_mails()