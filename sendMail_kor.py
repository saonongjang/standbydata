# -*- coding:utf-8 -*-
import os, smtplib
from email.MIME.Multipart import MIMEMultipart
from email.MIME.Base import MIMEBase
from email.MIME.Text import MIMEText
from email.header import Header
from email import Encoders
import time
import datetime
import random

gmail_username="홍길동"
gmail_user="hong@gmail.com"
gmail_pwd="**************"
attach_file=None

def send_gmail(to, subject, text, html, attach):
    msg=MIMEMultipart('alternative')
    msg['From']=gmail_username
    msg['To']=to
    msg['Subject']=Header(subject,'utf-8') #encoding
    msg.attach(MIMEText(text, 'plain', 'utf-8')) #encoding
    msg.attach(MIMEText(html, 'html', 'utf-8')) #encoding
    
    #첨부파일을 보내신다면 아래에서 #글자를 지워주세요.
    #part=MIMEBase('application','octet-stream')
    #part.set_payload(open(attach, 'rb').read())
    #Encoders.encode_base64(part)
    #part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
    #msg.attach(part)
    
    mailServer=smtplib.SMTP("smtp.gmail.com",587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user,gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()


def mainLoop():

    f = open("text.txt", "r")
    message = f.read()
    f.close()

    f = open("html.html", "r")
    html = f.read()
    f.close()
    
    title="단체메일 보내기 테스트"

    print ("Program Ready")
    print ("----------------------")
    f = open("list.txt", "r")
    emails = f.readlines()
    for email in emails:
        rand = random.randrange(1,5)       # Set range of the waiting time.
        email = email.strip()                # Removing White spaces.
        if email == "" :
            continue
        print ("[" + str(datetime.datetime.now()) + "] Sending email to " + email + "...")
        try:
            send_gmail(email,title,message,html,attach_file)
        except:
            print ("Mail sending error. (" + email + ")")
            break
        print ("[" + str(datetime.datetime.now()) + "] Complete... Waiting for " + str(rand) +" seconds.")
        time.sleep(rand)

    print ("Sending mail program is going to be terminated. Now waiting your command to exit." )
    time.sleep(-1)


if __name__ == "__main__":
    mainLoop()    

