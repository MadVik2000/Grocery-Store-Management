import CodeGenerator
import SendSms
import os
import time


def check_sms(phone_number):
    tries = 3
    code = CodeGenerator.gen_code()
    SendSms.send_sms(phone_number, code)

    print("We've Send A Code To Your Registered Phone Number!")

    while True:

        print("Please Enter The Code Here!")
        enter_code = input()
        os.system('cls')

        if enter_code.isnumeric():

            if int(enter_code) == code:
                print("Phone Number Successfully Verified!")
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
