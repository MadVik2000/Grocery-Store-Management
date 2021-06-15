from twilio.rest import Client

account_sid = 'AC4da9729d11774f453d165cefa6ba1852'

auth_token = '37423d5dd2e5967caacc6ff3ca2bd5e7'

client = Client(account_sid, auth_token)

def send_sms(phone_number, code):
    message = (
    f"Hey, You've Requested To Create An Account On Grocery Management System.\nPlease Enter This Code To Register Yourself:\n {code}\n\n Do Not Share This Code With Anyone Else! Ignore If You Haven't Requested To Register")

    client.messages.create(
        to= phone_number,
        from_='+19542660728',
        body= message 
    )
