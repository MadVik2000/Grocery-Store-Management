import db
import os,time
import User, CheckMail, CheckSms
import getpass
import GenerateSalt, Encrypter

def show_profile(id):
    print("User Profile\n\n")
    
    db.mycursor.execute('select user_name, email, phone_number, default_permission from users where user_id = %s;', [id])
    profile = db.mycursor.fetchone()
    
    print(f"User Id: {id}")
    print(f"User Name: {profile[0]}")
    print(f"Email: {profile[1]}")
    print(f"Phone Number: {profile[2]}")
    print(f"Default Permission For All Friends To See List: {profile[3]}")
    print('Press Enter To Continue')
    input()
    os.system('cls')
    
    if profile[1] == None:
        while True:
            print("\n\nYou Haven't Provided Your Email Id. Do you Want To Add It?")
            cho = input("Press y for Yes and n for No").lower()
            os.system('cls')
            if cho in ['y','n']:
                if cho == 'y':
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
                    
                    tries = 3
                    while True:
                        passwd = getpass.getpass('Please Enter Your Password To Confirm!\nNote That Your Password Would Not Be Visible While Typing\n')
                        os.system("cls")
                        salt = GenerateSalt.generate_salt(profile[0])

                        e_pass = Encrypter.give_hex(passwd, salt)
                        
                        if User.check_pass(profile[0], e_pass):
                            
                            db.mycursor.execute("update users set phone_number = %s where user_id = %s", [mail_id, id])
                            

                            print(f"You Have Added Your Email Address Successfully!!")
                            time.sleep(1)
                            os.system("cls")
                            break

                        else:
                            tries -= 1
                            if tries == 0:
                                print("You Are Out Of Tries! Please Try To Add Email After Some Time!")
                                time.sleep(1)
                                os.system("cls")
                                break

                            print(f"Wrong PassWord! {tries} More Tries Left")
                            time.sleep(1)
                            os.system("cls")
                
                    break
            
            else:
                print("Wrong Choice!")
                time.sleep(1)
                os.system('cls')
                
    if profile[2] == None:
        while True:
            print("\n\nYou Haven't Provided Your Phone Number. Do you Want To Add It?")
            cho = input("Press y for Yes and n for No").lower()
            os.system('cls')
            if cho in ['y', 'n']:
                if cho == 'y':
                    print("Please Enter Your Phone Number!")
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

                    tries = 3
                    while True:
                        passwd = getpass.getpass('Please Enter Your Password To Confirm!\nNote That Your Password Would Not Be Visible While Typing\n')
                        os.system("cls")
                        salt = GenerateSalt.generate_salt(profile[0])

                        e_pass = Encrypter.give_hex(passwd, salt)

                        if User.check_pass(profile[0], e_pass):
                            
                            db.mycursor.execute("update users set phone_number = %s where user_id = %s", [phone_number, id])
                            

                            print(f"You Have Added Your Phone Number Successfully!!")
                            time.sleep(1)
                            os.system("cls")
                            break

                        else:
                            tries -= 1
                            if tries == 0:
                                print("You Are Out Of Tries! Please Try To Add Email After Some Time!")
                                time.sleep(1)
                                os.system("cls")
                                break

                            print(f"Wrong PassWord! {tries} More Tries Left")
                            time.sleep(1)
                            os.system("cls")
                    
                break

            else:
                print("Wrong Choice!")
                time.sleep(1)
                os.system('cls')