import User,Encrypter
import os, time
import getpass
import GenerateSalt

def login(username):

    if User.check_user(username):
        tries = 3
        while True:
            passwd = getpass.getpass('Please Enter Your Password\nNote That Your Password Would Not Be Visible While Typing\n')
            os.system("cls")
            salt = GenerateSalt.generate_salt(username)
            
            e_passwd = Encrypter.give_hex(passwd, salt)
            
            if User.check_pass(username, e_passwd):

                print(f"Welcome {username}, You Have Logged Into Your Account!")
                time.sleep(1)
                os.system("cls")
                
                return True

            else:
                tries -= 1
                if tries == 0:
                    print("You Are Out Of Tries! Please Try To L̥og In After Some Time!")
                    time.sleep(1)
                    os.system("cls")
                    
                    return False

                print(f"Wrong PassWord! {tries} More Tries Left")
                time.sleep(1)
                os.system("cls")

    else:
        print("User Not Registered")
        time.sleep(1)
        os.system("cls")
        return False
