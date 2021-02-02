
import smtplib
from email.mime.text import MIMEText

me='gabrielyoon7@gmail.com'
you='gabrielyoon7@kyonggi.ac.kr'
contents='this is test email'

msg=MIMEText(contents, _charset='euc-kr')
msg['Subject']='동창회 모임'
msg['From']=me
msg['To']=you

server=smtplib.SMTP('gabrielyoon7@gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login("gabrielyoon7@gmail.com", "dbswngus96")

server.sendmail(me,you,msg.as_string())
server.quit
