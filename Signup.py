import Encrypter
import User
import CheckMail, CheckSms
import os, time
import getpass
import GenerateSalt
import db

def signup():
    while True:
        print("Please Enter Your UserName")
        username = input()
        os.system("cls")

        if User.check_user(username):
            print("User AlreadY Exists! Please Choose A Different Username")
            time.sleep(1)
            os.system("cls")
            
            break
        
        
        while True:
            print("We Need To Verify You!")
            print("You Can Verify Yourself Either By Email Address Or By Phone Number!")
            print("Press 1 for Email")
            print("Press 2 for Phone Number")
            inp = input()
            os.system('cls')
            
            if inp.isnumeric() and int(inp) in range(1,3):
                
                if int(inp) == 1:
                    while True:
                        print("Please Enter Your Email Id")
                        mail_id = input()
                        os.system("cls")

                        if not User.check_mail(mail_id):
                            time.sleep(1)
                            os.system("cls")
                            
                            break
                        
                        if not CheckMail.check_mail(mail_id):
                            print("Email Can't Be Verified! User Not Registered!")
                            time.sleep(1)
                            os.system("cls")
                            
                            break

                        passwd = getpass.getpass('Please Enter Your Password\nNote That Your Password Would Not Be Visible While Typing\n')
                        os.system("cls")
                        salt = GenerateSalt.generate_salt(username)
                        
                        e_pass = Encrypter.give_hex(passwd, salt)

                        db.mycursor.execute("insert into users (user_name, email, passwd) values (%s, %s, %s)", [username, mail_id, e_pass])
                        
                        print("You've Successfully Signed Up!\nPlease Login To Proceed!")
                        time.sleep(1)
                        os.system("cls")
                        
                        break
                    
                if int(inp) == 2:
                    while True:
                        print("Please Enter Your Mobile Number")
                        print("Don't Forget To Enter Your Country Code before your phone number")
                        print("+91 for India and +1 for USA and many more")
                        phone_number = input()
                        os.system('cls')
                        
                        if not User.check_phone(phone_number):
                            time.sleep(1)
                            os.system("cls")

                            break
                        
                        if not CheckSms.check_sms(phone_number):
                            print("Phone Number Can't Be Verified! User Not Registered!")
                            time.sleep(1)
                            os.system("cls")

                            break
                    
                        passwd = getpass.getpass('Please Enter Your Password\nNote That Your Password Would Not Be Visible While Typing\n')
                        os.system("cls")
                        salt = GenerateSalt.generate_salt(username)

                        e_pass = Encrypter.give_hex(passwd, salt)

                        db.mycursor.execute("insert into users (user_name, phone_number, passwd) values (%s, %s, %s)", [username, phone_number, e_pass])
                        
                        print("You've Successfully Signed Up!\nPlease Login To Proceed!")
                        time.sleep(1)
                        os.system("cls")

                        break
                
                break
            
            else:
                print("Wrong Choice! Please Enter Either 1 or 2")
                time.sleep(1)
                os.system('cls')
                continue
            
                
        break
