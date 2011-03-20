#import smtplib
#import xmpp
import sys
import time
from django.core.mail import send_mail
#from django.core import mail

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


def send_email(sender, to, subject, content):
    message = content
    send_mail(subject, message, sender, [to], fail_silently=False)
