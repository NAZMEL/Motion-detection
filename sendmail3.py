import smtplib, getpass, sys

from email.mime.text import MIMEText
from email.header    import Header

# class Mail_Sender(object):
#     def __init__(self):
#         self.smtp_host = 'smtp.gmail.com'  

#         print("Enter person\'s data of mail-post sending: ") 
#         self.login = input("Enter address of server: ").strip()
#         self.password = getpass.getpass("Enter password: ").strip()
#         Getter = input('Enter person\'s email getting the letter: ').strip()
#         self.recipients_emails = [Getter]

#         self.msg = MIMEText('Your login is confirmed!', 'plain', 'utf-8')

#         self.messageInitials()
        
#         self.s = smtplib.SMTP(self.smtp_host, 587, timeout=10)
#         self.s.set_debuglevel(1)
        
            


#     def messageInitials(self):
#         self.msg['Subject'] = Header('Motion detected', 'utf-8')
#         self.msg['From'] = self.login
#         self.msg['To'] = ", ".join(self.recipients_emails)
#         while 1:
#             try:
#                 self.s.starttls()
#                 self.s.login(self.login, self.password)
#                 self.s.sendmail(self.msg['From'], self.recipients_emails, self.msg.as_string())
#                 print("Letter was send!")
#                 break
#             except:
#                 print("Error sending letter!\nYour email login or password is incorrect!\nTry again!\n")
        

        
        
#     def sendLetter(self): 
#         self.msg = MIMEText('Motion detected in the middle of location!!!', 'plain', 'utf-8')
#         try:
#             self.s.sendmail(self.msg['From'], self.recipients_emails, self.msg.as_string())
#             print("Letter was sent!")
#         except:
#             print("Error sending letter! ")
            

#     def sendClose(self):
#         self.s.close()






smtp_host = 'smtp.gmail.com'        
print("Enter person\'s data of mail-post sending: ") 
login = input("Enter address of server: ")
password = getpass.getpass("Enter password: ")
recipients_emails = [login]

msg = MIMEText('Пирвіт всім', 'plain', 'utf-8')
msg['Subject'] = Header('subject…', 'utf-8')
msg['From'] = login
msg['To'] = ", ".join(recipients_emails)

s = smtplib.SMTP(smtp_host, 587, timeout=10)
s.set_debuglevel(1)
try:
    s.starttls()
    s.login(login, password)
    s.sendmail(msg['From'], recipients_emails, msg.as_string())
finally:
    s.quit()