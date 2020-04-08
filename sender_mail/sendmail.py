import smtplib, getpass, socket, sys, os
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime as dt

class Mail_Sender(object):
    
    def __init__(self):
        # connect to the server
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            
        except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as error:
            print('Connectioin to Gmail-server is failed!!!')
            print(error)
            getpass.getpass('Press ENTER to continue...')
            sys.exit(1) #exit
        else:
            print()
            print('Connection to Gmail-server is succesfully!!!\n')
        
        
        self.msg = MIMEMultipart()
        self.entersData()


        
    def entersData(self):
        while 1:
            try:
                #self.sender_login = str(input("Enter address of server: ")).strip()
                #self.sender_password = str(getpass.getpass("Enter password: ")).strip() 
                self.sender_login = 'open.cv18@gmail.com'
                self.sender_password = 'open.cv18ukr'
                self.server.login(self.sender_login, self.sender_password)
                break
            except smtplib.SMTPAuthenticationError:
                print('\nYour email login or password is incorrect!\nTry again!\n')
        

        self.TO = str(input('Enter person\'s email getting the letter: ')).strip()
        '''
        self.SUBJECT = 'Motion Detection'
        #self.CONTENT = str(input('Enter content of letter: ')).strip()
        self.CONTENT = "Motion detected in the middle of location!!!"

        self.BODY = '\r\n'.join([
        'TO: %s' % self.TO,
        'From: %s' % self.sender_login, 
        'Subject: %s' % self.SUBJECT,
        ' ',
        self.CONTENT
        ])
        '''
        self.msg['Subject'] = 'Motion detection'
        self.msg['To'] = self.TO
        self.msg.preamble = 'Your login is confirmed!'
        #self.msg.attach(MIMEText('Your login is confirmed!'))

        while 1: 
            try:
               
                #self.server.sendmail(self.sender_login, [self.TO], '\r\n'.join(['TO: %s' % self.TO, 'From: %s' % self.sender_login,  'Subject: %s' % self.SUBJECT, ' ', 'Your login is confirmed!']))
                self.server.sendmail(self.sender_login, [self.TO], self.msg.as_string())
                print('Letter confirmed have sent.')
                self.msg.preamble = 'Motion detected in the middle of location!!!'
                break
            except:
                print('Error sending letter!')
                print('Perhaps input getting email is wrong. Try again!')
                self.TO = str(input('Enter email which will getting the letter: ')).strip()
    


    def sendLetter(self):
        try:
            #self.server.sendmail(self.sender_login, [self.TO], self.BODY)
            self.server.sendmail(self.sender_login, [self.TO], self.msg.as_string())
            print('Letter have sent. At {0}.'.format(dt.now().strftime('%d:%m:%Y-%Hh:%Mm:%Ss')))
        except:
            print('Error sending letter!')
    
    def AddImageSend(self, _imgFileName = 'frame.jpg'):
        img_data = open(_imgFileName, 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename(_imgFileName))
        self.msg.attach(image)
                
    def sendClose(self):
        self.server.close()



