import smtplib
from email.mime.text import MIMEText
def send_email(message,subject,toaddrs):
    fromaddr = 'kellytrong112@gmail.com'
    username = 'kellytrong112@gmail.com'
    password = 'trong0924707771'
    msg = MIMEText(message, 'html')
    msg['Subject']  = subject
    msg['From']=fromaddr
    msg['Reply-to'] = 'no-reply'
    msg['To'] = toaddrs
    server = smtplib.SMTP('smtp.gmail.com:587')
    #Go to Google's Account Security Settings: www.google.com/settings/security
    #Find the field "Access for less secure apps". Set it to "Allowed".
    try:
        server.starttls()
        server.login(username,password)
    except Exception,e:
        print str(e)
    server.sendmail(fromaddr, [toaddrs], msg.as_string())
    server.quit()
subject = raw_input("Enter your subject?: ")
message = raw_input("Enter your mesage?: ")
toaddrs = raw_input("Enter receiver email address?: ")

try:
    send_email(str(message),str(subject),str(toaddrs))
except Exception,e:
    print str(e)