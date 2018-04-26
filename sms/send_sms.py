import os
from twilio.rest import Client #Download the twilio-python library from twilio.com


account_sid = "AC049fae2e652501bf8fae0d56d1a70a57"
auth_token = "101675dc42058f00995e14e9c071f5d1"

client = Client(account_sid, auth_token)

client.messages.create(
    to="9723337434",
    from_ = "+14696091218",
    body= "Welcome to this crazy place.You are going die!",
)