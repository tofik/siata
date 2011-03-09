import xmpp
import sys
import time

def send_im_chat(content, recipient):
    login = 'tofikowy03' # @gmail.com
    pwd   = 'astral123'
    cnx = xmpp.Client('gmail.com',debug=[])
    cnx.connect( server=('talk.google.com',5223) )
    cnx.auth(login,pwd, 'botty')
    message = xmpp.Message(recipient) 
    message.setAttr('type', 'chat')
    message.setBody(content)
    cnx.send(message)

