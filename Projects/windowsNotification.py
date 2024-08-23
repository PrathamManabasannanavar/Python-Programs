from plyer import notification;
import smtplib;
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time

notification.notify(
    title="Greeting user",
    message="Email will be sent",
    timeout=6
)
current_time = time.localtime()

#sending a mail to myself when anybody loggs in my PC
sender_email = '190vpu2pratham@gmail.com'
receiver_email = 'pratham29052004@gmail.com'
password = os.getenv("PythonEmailPass")

subject = "Windows Login Notifcation Email"
body = f"{os.getlogin()} user logged in to your PC at {current_time.tm_mday}/{current_time.tm_mon}/{current_time.tm_year}\t{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}"
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['subject'] = subject
msg.attach(MIMEText(body, 'plain'))

print(body)
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("sucessfully sent")
except Exception as e:
    print('unsucessful attempt', e)