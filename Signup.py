import Encrypter
import mysql.connector
import User
import CheckMail
import os, time
import getpass
import GenerateSalt

mydb = mysql.connector.connect(host='localhost', user='user1', passwd='passwd', database='project')
mycursor = mydb.cursor()

def signup():
    while True:
        print("Please Enter Your UserName")
        username = input()
        os.system("cls")

        if User.check_user(username):
            print("User AlreadY Exists! Please Choose A Different Username")
            time.sleep(1)
            os.system("cls")
            
            continue

        while True:
            print("Please Enter Your Email Id")
            mail_id = input()
            os.system("cls")

            if not User.check_mail(mail_id):
                print("Email Standards Not Met")
                time.sleep(1)
                os.system("cls")
                
                continue
            
            if not CheckMail.check_mail(mail_id):
                print("Email Can't Be Verified! User Not Registered!")
                time.sleep(1)
                os.system("cls")
                
                break

            passwd = getpass.getpass(
                'Please Enter Your Password\nNote That Your Password Would Not Be Visible While Typing\n')
            os.system("cls")
            salt = GenerateSalt.generate_salt(username)
            
            e_pass = Encrypter.give_hex(passwd, salt)

            mycursor.execute("insert into users (user_name, email, passwd) values (%s, %s, %s)", [username, mail_id, e_pass])
            mydb.commit()
            print("You've Successfully Signed Up!\nPlease Login To Proceed!")
            time.sleep(1)
            os.system("cls")
            
            break

        break
