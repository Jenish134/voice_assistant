from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
def mail_sender1():
    print('speak anything .......')
    # create message object instance
    msg = MIMEMultipart()
    
    print('openaing mail sender')
    message = input('enter your message here :-')
    
    # setup the parameters of the message
    password = "jedeepatel121051412198A@"
    msg['From'] = "jedeepatel12@gmail.com"
    msg['To'] = input('enter your mail id  here :-')
    msg['Subject'] = input('enter your subject here :-')
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    
    print ("successfully sent email to %s:" % (msg['To']))


mail_sender1()