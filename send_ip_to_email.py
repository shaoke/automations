import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import socket
import fcntl
import struct
import threading

# Change to your own account information
# Account Information
to = 'shaoxu@tibco.com' # Email to send to.
gmail_user = 'uxtest0001@gmail.com' # Email to send from. (MUST BE GMAIL)
gmail_password = 'skuxtest' # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com:587') # Server to use.
REMOTE_SERVER = "www.google.com"

def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
    pass
  return False

def get_ip_address(ifname):
  ip = ''
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = socket.inet_ntoa(fcntl.ioctl(
      s.fileno(),
      0x8915,  # SIOCGIFADDR
      struct.pack('256s', ifname[:15])
    )[20:24])
  except:
    print 'Get ip error'

  return ip

def sendEmail():
  # set default value
  eth0 = get_ip_address('eth0')
  wlan0 = get_ip_address('lo')

  smtpserver.ehlo()  # Says 'hello' to the server
  smtpserver.starttls()  # Start TLS encryption
  smtpserver.ehlo()
  smtpserver.login(gmail_user, gmail_password)  # Log in to server
  today = datetime.date.today()  # Get current time/date

  # Creates the text, subject, 'from', and 'to' of the message.
  msg = MIMEText('eth0:'+eth0+'\n'+'wlan0'+wlan0)
  msg['Subject'] = 'IPs For RaspberryPi on %s' % today.strftime('%b %d %Y')
  msg['From'] = gmail_user
  msg['To'] = to
  # Sends the message
  smtpserver.sendmail(gmail_user, [to], msg.as_string())
  # Closes the smtp server.
  smtpserver.quit()

def checkWhetherOnline():
  # do something here ...
  # call f() again in 60 seconds
  if is_connected():
    sendEmail()
    print 'online'
  else:
    print 'offline'
    threading.Timer(60, checkWhetherOnline).start()

checkWhetherOnline()