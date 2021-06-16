import User
import os,time
import db

def view_requests(id):
    db.mycursor.execute(
        "select r.from_id, u.user_name from requests r join users u on r.from_id = u.user_id where r.to_id = %s", [id])
    result = db.mycursor.fetchall()

    if not result:
        print("No Friend Requests!")
        time.sleep(1)
        os.system("cls")
        return

    for res in result:
        print("%-5s %-12s" % (res[0], res[1]))
        
    input("Press Enter To Continue")    
    os.system("cls")
    
def check_friend(id):
    db.mycursor.execute(
        "select r.from_id, u.user_name from requests r join users u on r.from_id = u.user_id where r.to_id = %s", [id])
    result = db.mycursor.fetchone()
    if result:
        return True
    
    return False

def request_approval(id):
    if not check_friend(id):
        print("No Friend Request Are There")
        time.sleep(1)
        os.system('cls')
        return
    
    while True:
        print("1. View Friend Requests")
        print("2. Accept A Request")
        print("3. Reject A Request")
        print("4. Leave")

        while True:
            choice = input("Please Enter Your Choice!")
            if choice.isnumeric() and int(choice) in range(1, 5):
                if int(choice) == 4:
                    return
                
                if int(choice) == 1:
                    view_requests(id)
                    break

                if int(choice) == 2:
                    accept_request(id)
                    break

                if int(choice) == 3:
                    reject_request(id)
                    break
                
            print("Please Enter A Valid Choice")
            time.sleep(1)
            os.system("cls")

        db.mycursor.execute('select * from requests where to_id = %s', [id])
        result = db.mycursor.fetchall()
        if not result:
            print("No Friends Requests Left!")
            time.sleep(1)
            os.system("cls")
            break


def send_request(id):
    while True:
        send_id = input("Please Enter The User ID You Want To Send Request To!")
        os.system("cls")
        
        if send_id.isnumeric():
            if id == int(send_id):
                print("You're your own buddy! Try Finding More Friends!")
                time.sleep(1)
                os.system('cls')
                return
            
            if User.check_user_id(send_id):

                db.mycursor.execute('select * from friends where friend_one = %s and friend_two = %s', [id, int(send_id)])
                result = db.mycursor.fetchone()
                if result:
                    print("You're Already Friend With That User!")
                    time.sleep(1)
                    os.system("cls")
                    
                    return
                
                db.mycursor.execute('select * from requests where to_id = %s and from_id = %s', [int(send_id), id])
                result = db.mycursor.fetchone()
                if result:
                    print("Request Already Send!")
                    time.sleep(1)
                    os.system("cls")
                    
                    return

                db.mycursor.execute('select * from requests where to_id = %s and from_id = %s', [id, int(send_id)])
                result = db.mycursor.fetchone()
                if result:
                    print("User Has Already Send You A Request! Please Accept To Add As Friend!")
                    time.sleep(1)
                    os.system("cls")
                    
                    return
                
                db.mycursor.execute('insert into requests (to_id, from_id) values (%s, %s);', [int(send_id), id])

                
                print("Friend Request Send!")
                time.sleep(1)
                os.system("cls")

                break

            print("User Doesn't Exist!")
            time.sleep(1)
            os.system("cls")
            
            
        print("Please Enter A Valid User Id")
        time.sleep(1)
        os.system('cls')


def accept_request(id):
    while True:
        print("Enter The User Id To Accept Request")
        choice = input()
        os.system("cls")
        
        if choice.isnumeric():
            db.mycursor.execute(
                'select * from requests where to_id = %s and from_id = %s', [id, int(choice)])
            result = db.mycursor.fetchone()
            if not result:
                print("Request Not Found!")
                time.sleep(1)
                os.system("cls")
                break
            
            db.mycursor.execute('select default_permission from users where user_id = %s', [id])
            one_permission = db.mycursor.fetchone()[0]
            
            db.mycursor.execute('select default_permission from users where user_id = %s', [int(choice)])
            two_permission = db.mycursor.fetchone()[0]

            db.mycursor.execute('insert into friends (friend_one, friend_two, permission) values (%s, %s, %s)', [
                             int(choice), id, two_permission])
            db.mycursor.execute('insert into friends (friend_one, friend_two, permission) values (%s, %s, %s)', [
                             id, int(choice), one_permission])
            db.mycursor.execute('delete from requests where to_id = %s and from_id = %s', [
                             id, int(choice)])
            
            break

        print("Wrong User ID!")
        time.sleep(1)
        os.system("cls")


def reject_request(id):
    while True:
        print("Enter The User Id To Reject Request")
        choice = input()
        if choice.isnumeric():
            db.mycursor.execute(
                'select * from requests where to_id = %s and from_id = %s', [id, int(choice)])
            result = db.mycursor.fetchone()
            if not result:
                print("Request Not Found!")
                time.sleep(1)
                os.system("cls")
                break

            db.mycursor.execute('delete from requests where to_id = %s and from_id = %s', [
                             id, int(choice)])
            
            break

        print("Wrong User ID!")
        time.sleep(1)
        os.system("cls")

