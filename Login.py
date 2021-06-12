import User,Encrypter
import os, time

def login(username):

    if User.check_user(username):
        tries = 3
        while True:
            print("Please Enter Your Password")
            passwd = input()
            os.system("cls")
            e_passwd = Encrypter.give_hex(passwd)
            if User.check_pass(username, e_passwd):

                print(f"Welcome {username}, You Have Logged Into Your Account!")
                time.sleep(1)
                os.system("cls")
                
                return True

            else:
                tries -= 1
                if tries == 0:
                    print("You Are Out Of Tries! Please Try To Log In After Some Time!")
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
