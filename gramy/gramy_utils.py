#import smtplib
#import xmpp
import sys
import time
from django.core.mail import send_mail
from google.appengine.api import mail
from django.core import mail

# def send_im_chat(content, recipient):
#     login = 'tofikowy03' # @gmail.com
#     pwd   = 'astral123'
#     cnx = xmpp.Client('gmail.com',debug=[])
#     cnx.connect( server=('talk.google.com',5223) )
#     cnx.auth(login,pwd, 'botty')
#     message = xmpp.Message(recipient) 
#     message.setAttr('type', 'chat')
#     message.setBody(content)
#     cnx.send(message)


def send_mail4play(decision, recipients):
    if decision == 0:
        werdykt = 'nie ma grania!'
        temat = 'nie gramy'
    if decision == 1:
        werdykt = 'jest granie!'
        temat = 'gramy'
    subject = temat
    content = werdykt
#    send_mail(subject, content,'korba@autograf.pl', recipients) # django.core

    mail.send_mail('tomek.filipczuk@gmail.com',recipients, subject, content)
