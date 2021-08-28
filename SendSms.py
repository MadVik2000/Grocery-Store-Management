from twilio.rest import Client
import os

client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

def send_sms(phone_number, code):
    message = (
    f"Hey, You've Requested To Create An Account On Grocery-Mania.\nPlease Enter This Code To Register Yourself:\n {code}\n\n Do Not Share This Code With Anyone Else! Ignore If You Haven't Requested To Register")

    client.messages.create(
        to= phone_number,
        from_='+19542660728',
        body= message 
    )
