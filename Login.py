import User,Encrypter

def login():
    print("Please Enter Your Username")
    username = input()
    if User.check_user(username):
        tries = 3
        while True:
            print("Please Enter Your Password")
            passwd = input()
            e_passwd = Encrypter.give_hex(passwd)
            if User.check_pass(username, e_passwd):

                print(f"Welcome {username}, You Have Logged Into Your Account!")
                
                return (username,True)

            else:
                tries -= 1
                if tries == 0:
                    print("You Are Out Of Tries! Please Try To Log In After Some Time!")
                    
                    return (username,False)

                print(f"Wrong PassWord! {tries} More Tries Left")

    else:
        print("User Not Registered")
        return False