import os
from twilio.rest import Client                               #Download the twilio-python library from twilio.com

#create an instance message
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

client.messages.create(
    to="",
    from_ = "",
    body= "Welcome to this crazy place.You are going die!",
)