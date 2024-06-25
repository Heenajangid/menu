#!/usr/bin/python3



import cgi

from twilio.rest import Client





print("Content-Type: text/html")

print()



# Twilio account credentials

account_sid = ''

auth_token = ''

client = Client(account_sid, auth_token)



# Get the form data

form = cgi.FieldStorage()

sender_number = form.getvalue('sender_number')

message_body = form.getvalue('message_body')









message = client.messages.create(

    body=message_body,

    to=sender_number,

    from_='+18542691324'  # provided by Twilio API

    )

print(message.sid)
