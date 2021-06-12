import CodeGenerator, SendMail
import os, time

def check_mail(mail_id):
    tries = 3
    code = CodeGenerator.gen_code()
    SendMail.verify_mail(mail_id, code)
    
    print("We've Send A Code To Your Registered Email Id!")
    
    while True:
        
        print("Please Enter The Code Here!")
        enter_code = input()
        os.system('cls')


        if enter_code.isnumeric():
        
            if int(enter_code) == code:
                print("Email Successfully Verified!")
                time.sleep(2)
                os.system('cls')
                
                return True

            else:
                print("You've Entered Wrong Code!")

        else:
            print("You've Entered Wrong Code")
            
        tries -= 1
        if tries == 0:
            print("Maximum Number Of Tries Reached!")
            
            return False

        print(f"You've {tries} left")
        continue
