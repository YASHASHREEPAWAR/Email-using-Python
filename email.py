import smtplib
from email.message import EmailMessage

#Create an Email Object
email = EmailMessage()
#set the Sender Name
email['from'] = ' '   #sender name
#set the receiver address
email['to'] = ' '    #receiver email
#set email subject
email['subject'] = ' '  #email subject
#set email content
email.set_content('')   #main_content
with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo() #waking up the server
    smtp.starttls() #Start Encryption
    smtp.login('', '') #user login credentials email-id and password
    smtp.send_message(email) #sending email
    print("All done!!!")
