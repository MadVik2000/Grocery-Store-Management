import mysql.connector
import User
import os,time

mydb = mysql.connector.connect(host='localhost', user='user1', passwd='passwd', database='project')
mycursor = mydb.cursor()

def view_requests(id):
    mycursor.execute(
        "select r.from_id, u.user_name from requests r join users u on r.from_id = u.user_id where r.to_id = %s", [id])
    result = mycursor.fetchall()

    if not result:
        print("No Friend Requests!")
        time.sleep(1)
        os.system("cls")
        return

    for res in result:
        print("%-5s %-12s" % (res[0], res[1]))
        
    input("Press Enter To Continue")    
    os.system("cls")
    


def request_approval(id):
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

        mycursor.execute('select * from requests where to_id = %s', [id])
        result = mycursor.fetchall()
        if not result:
            print("No Friends Requests Left!")
            time.sleep(1)
            os.system("cls")
            break


def send_request(id):
    while True:
        send_id = input("Please Enter The User ID You Want To Send Request To!")
        os.system("cls")
        
        if User.check_user(send_id):

            mycursor.execute('select * from friends where friend_one = %s and friend_two = %s', [id, send_id])
            result = mycursor.fetchone()
            if result:
                print("You're Already Friend With That User!")
                time.sleep(1)
                os.system("cls")
                
                return
            
            mycursor.execute('select * from requests where to_id = %s and from_id = %s', [int(send_id), id])
            result = mycursor.fetchone()
            if result:
                print("Request Already Send!")
                time.sleep(1)
                os.system("cls")
                
                return

            mycursor.execute('select * from requests where to_id = %s and from_id = %s', [id, int(send_id)])
            result = mycursor.fetchone()
            if result:
                print("User Has Already Send You A Request! Please Accept To Add As Friend!")
                time.sleep(1)
                os.system("cls")
                
                return
            
            mycursor.execute('insert into requests (to_id, from_id) values (%s, %s);', [int(send_id), id])

            mydb.commit()
            print("Friend Request Send!")
            time.sleep(1)
            os.system("cls")

            break

        print("User Doesn't Exist!")
        time.sleep(1)
        os.system("cls")


def accept_request(id):
    while True:
        print("Enter The User Id To Accept Request")
        choice = input()
        os.system("cls")
        
        if choice.isnumeric():
            mycursor.execute(
                'select * from requests where to_id = %s and from_id = %s', [id, int(choice)])
            result = mycursor.fetchone()
            if not result:
                print("Request Not Found!")
                time.sleep(1)
                os.system("cls")
                
                break

            mycursor.execute('insert into friends (friend_one, friend_two) values (%s, %s)', [
                             int(choice), id])
            mycursor.execute('insert into friends (friend_one, friend_two) values (%s, %s)', [
                             id, int(choice)])
            mycursor.execute('delete from requests where to_id = %s and from_id = %s', [
                             id, int(choice)])
            mydb.commit()
            break

        print("Wrong User ID!")
        time.sleep(1)
        os.system("cls")


def reject_request(id):
    while True:
        print("Enter The User Id To Reject Request")
        choice = input()
        if choice.isnumeric():
            mycursor.execute(
                'select * from requests where to_id = %s and from_id = %s', [id, int(choice)])
            result = mycursor.fetchone()
            if not result:
                print("Request Not Found!")
                time.sleep(1)
                os.system("cls")
                
                break

            mycursor.execute('delete from requests where to_id = %s and from_id = %s', [
                             id, int(choice)])
            mydb.commit()
            break

        print("Wrong User ID!")
        time.sleep(1)
        os.system("cls")

