import getpass
import Encrypter,User,CodeGenerator,SendMail,SendSms
import os, time
import GenerateSalt
import db

def forgot_passwd():
    print("Please Enter Your UserName")
    username = input()
    os.system("cls")

    if User.check_user(username):

        tries = 3
        db.mycursor.execute('select email from users where user_name = %s', [username])
        mail_id = db.mycursor.fetchone()
        
        if mail_id[0]:
            code = CodeGenerator.gen_code()

            SendMail.send_mail(mail_id[0], code)
            print("We've Send A Code To Your Registered Email Id!")
            while True:
                print("Please Enter The Code Here!")
                enter_code = input()
                os.system("cls")

                if enter_code.isnumeric():

                    if int(enter_code) == code:
                        change_password(username)
                        break

                    else:
                        print("You've Entered Wrong Code!")
                    
                else:
                    print("You've Entered Wrong Code")
                    
                tries -= 1
                if tries == 0:
                    print("Maximum Number Of Tries Reached!")
                    print("Try Later")
                    time.sleep(1)
                    os.system("cls")
                    
                    break

                print(f"Wrong Code! You've {tries} left")
                time.sleep(1)
                os.system("cls")
                
                continue
            
        else:   
            db.mycursor.execute('select phone_number from users where user_name = %s', [username])
            phone_number = db.mycursor.fetchone()[0]
            
            code = CodeGenerator.gen_code()

            SendSms.send_sms(phone_number, code)
            print("We've Send A Code To Your Registered Phone Number!")
            while True:
                print("Please Enter The Code Here!")
                enter_code = input()
                os.system("cls")

                if enter_code.isnumeric():

                    if int(enter_code) == code:
                        change_password(username)
                        break

                    else:
                        print("You've Entered Wrong Code!")

                else:
                    print("You've Entered Wrong Code")

                tries -= 1
                if tries == 0:
                    print("Maximum Number Of Tries Reached!")
                    print("Try Later")
                    time.sleep(1)
                    os.system("cls")

                    break

                print(f"Wrong Code! You've {tries} left")
                time.sleep(1)
                os.system("cls")

                continue


    else:
        print("No User Exists")
        time.sleep(1)
        os.system("cls")
        


def change_password(username):
    passwd = getpass.getpass('Please Enter Your Password\nNote That Your Password Would Not Be Visible While Typing\n')
    os.system("cls")
    salt = GenerateSalt.generate_salt(username)
    
    e_pass = Encrypter.give_hex(passwd, salt)

    db.mycursor.execute('update users set passwd = %s where user_name = %s', [e_pass, username])
    
    print("Password Changed Successfully!")
    print("Please Log In To Proceed!")
    time.sleep(1)
    os.system("cls")
