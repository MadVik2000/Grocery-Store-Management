import mysql.connector
import Encrypter,User,CodeGenerator,SendMail

mydb = mysql.connector.connect(host='localhost', user='user1', passwd='passwd', database='project')
mycursor = mydb.cursor()

def forgot_passwd():
    print("Please Enter Your UserName")
    username = input()

    if User.check_user(username):

        tries = 3
        mycursor.execute(
            'select email from users where user_name = %s', [username])
        mail_id = mycursor.fetchone()[0]
        code = CodeGenerator.gen_code()

        SendMail.send_mail(mail_id, code)
        print("We've Send A Code To Your Registered Email Id!")
        while True:
            print("Please Enter The Code Here!")
            enter_code = input()

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
                break

            print(f"Wrong Code! You've {tries} left")
            continue

    else:
        print("No User Exists")


def change_password(username):
    print("Please Enter Your New Password!")
    passwd = input()
    e_pass = Encrypter.give_hex(passwd)

    mycursor.execute('update users set passwd = %s where user_name = %s', [
                     e_pass, username])
    mydb.commit()
    print("Password Changed Successfully!")
    print("Please Log In To Proceed!")