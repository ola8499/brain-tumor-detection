import win32com.client as win32
import sys
import smtplib
import os

email = sys.argv[1]
name = sys.argv[2]
surname = sys.argv[3]
id = sys.argv[4]
detector = sys.argv[5]
percent = sys.argv[6]
print(email, name, id, detector, percent)

sender = "atanska08@gmail.com"
receiver = email

message = f"""\
Subject: Brain Tumor Detection - Result
To: {receiver}
From: {sender}

Result from Brain Tumor Detector
Person:{name} {surname}
Personal ID Number: {id}
Result:
{name} {surname} {detector} a brain tumor with {str(percent)}% confidence."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("0b57610263a21e", "706b40730021d6")
    server.sendmail(sender, receiver, message)

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = email
mail.Subject = 'Brain Tumor Detection - Result'

mail.HTMLBody = f"<h1>Result from Brain Tumor Detector</h1><br>Person:{name} {surname}<br>Personal ID Number: {id}<br><br> Result:{name} {surname} {detector} a brain tumor with {str(percent)}% confidence.<br><br><br>"
if len(os.listdir('pdf-files'))!=0:
    for file in os.listdir('pdf-files'):
        attachment = 'pdf-files' + "/" + file
        mail.Attachments.Add(attachment)
mail.Send()
