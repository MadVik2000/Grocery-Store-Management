import smtplib
import os

def send_mail(mail_id, code):
    os.system("cls")

    message = (
        f"Hey, You've Requested To Change Your Password as you've forgotten your password!\nPlease Enter This Code To Change Your Password:\n {code}\n\n Do Not Share This Code With Anyone Else! Ignore If You Haven't Requested To Change Your Password")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.environ["SENDING_MAIL"], os.environ["SENDING_MAIL_PASSWORD"])

    server.sendmail(os.environ["SENDING_MAIL"], mail_id, message)
    
    
def verify_mail(mail_id, code):
    os.system('cls')

    message = (
        f"Hey, You've Requested To Create An Account On Grocery Store Management System.\nPlease Enter This Code To Register Yourself:\n {code}\n\n Do Not Share This Code With Anyone Else! Ignore If You Haven't Requested To Register")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.environ["SENDING_MAIL"], os.environ["SENDING_MAIL_PASSWORD"])

    server.sendmail(os.environ["SENDING_MAIL"], mail_id, message)
