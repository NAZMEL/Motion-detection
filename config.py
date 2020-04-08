PORT = "465"  # for SSL
SMTP_SERVER = "smtp.gmail.com"
FILE_RECEIVERS = "sources/receiver.csv"

SENDER_EMAIL = ""  # Your addres of address of your company
SENDER_PASSWORD = ""       # Your password of address

MESSAGE = """\
Subject: MOVE DETECTED

Hi, {name}!\n Detector has fixed any move in your location. Check it!
"""

# delay between a sent messages in seconds
DELAY_SEND = 30

# colors for ouptput sckripts
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'