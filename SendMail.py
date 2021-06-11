import smtplib

def send_mail(mail_id, code):
    my_mail = 'madvik143@gmail.com'
    my_pass = input("Enter Your Mail Password")

    message = (
        f"Hey, You've Requested To Change Your Password as you've forgotten your password!\nPlease Enter This Code To Change Your Password:\n {code}\n\n Do Not Share This Code With Anyone Else! Ignore If You Haven't Requested To Change Your Password")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_mail, my_pass)

    server.sendmail(my_mail, mail_id, message)
    
    
def verify_mail(mail_id, code):
    my_mail = 'madvik143@gmail.com'
    my_pass = input("Enter Your Mail Password")

    message = (
        f"Hey, You've Requested To Create An Account On List Management System.\nPlease Enter This Code To Register Yourself:\n {code}\n\n Do Not Share This Code With Anyone Else! Ignore If You Haven't Requested To Register")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_mail, my_pass)

    server.sendmail(my_mail, mail_id, message)
