import Encrypter
import mysql.connector
import User
import CheckMail

mydb = mysql.connector.connect(host='localhost', user='user1', passwd='passwd', database='project')
mycursor = mydb.cursor()

def signup():
    while True:
        print("Please Enter Your UserName")
        username = input()

        if User.check_user(username):
            print("User AlreadY Exists! Please Choose A Different Username")
            continue

        while True:
            print("Please Enter Your Email Id")
            mail_id = input()

            if not User.check_mail(mail_id):
                print("Email Standards Not Met")
                continue
            
            if not CheckMail.check_mail(mail_id):
                print("Email Can't Be Verified! User Not Registered!")
                break

            print("Please Enter Your Password")
            passwd = input()
            e_pass = Encrypter.give_hex(passwd)

            mycursor.execute("insert into users (user_name, email, passwd) values (%s, %s, %s)", [
                             username, mail_id, e_pass])
            mydb.commit()
            print("You've Successfully Signed Up!\nPlease Login To Proceed!")
            break

        break
