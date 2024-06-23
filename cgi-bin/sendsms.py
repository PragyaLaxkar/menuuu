#!/usr/bin/python3
print("Content-type: text/html")
print("\n")

from twilio.rest import Client
import cgi

form = cgi.FieldStorage()
body = form.getvalue("body")

account_sid = 'ACb6728ca2e0687ace0d67f4022289e73e'
auth_token = '073e8a174aa338f384f1cf78c050d989'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = body,
    from_='+17372607738',
    to="+916377097964"
)

print(message.body)