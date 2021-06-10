import mysql.connector
import User
mydb = mysql.connector.connect(host='localhost', user='user1', passwd='passwd', database='project')

mycursor = mydb.cursor()

def view_requests(id):
    mycursor.execute(
        "select r.from_id, u.user_name from requests r join users u on r.from_id = u.user_id where r.to_id = %s", [id])
    result = mycursor.fetchall()

    if not result:
        print("No Friend Requests!")
        return

    for res in result:
        print("%-5s %-12s" % (res[0], res[1]))

    request_approval(id)


def request_approval(id):
    while True:
        print("1. Accept A Request")
        print("2. Reject A Request")
        print("3. Leave")

        while True:
            choice = input("Please Enter Your Choice!")
            if choice.isnumeric() and int(choice) in range(1, 4):
                if int(choice) == 3:
                    return

                if int(choice) == 1:
                    accept_request(id)
                    break

                if int(choice) == 2:
                    reject_request(id)
                    break

        mycursor.execute('select * from requests where to_id = %s', [id])
        result = mycursor.fetchall()
        if not result:
            print("No Friends Requests Left!")
            break


def send_request(id):
    while True:
        send_id = input(
            "Please Enter The User ID You Want To Send Request To!")
        if User.check_user(send_id):

            mycursor.execute('select * from friends where friend_one = %s and friend_two = %s', [id, send_id])
            result = mycursor.fetchone()
            if result:
                print("You're Already Friend With That User!")
                return
            
            mycursor.execute(
                'select * from requests where to_id = %s and from_id = %s', [int(send_id), id])
            result = mycursor.fetchone()
            if result:
                print("Request Already Send!")
                return

            mycursor.execute(
                'select * from requests where to_id = %s and from_id = %s', [id, int(send_id)])
            result = mycursor.fetchone()
            if result:
                print(
                    "User Has Already Send You A Request! Please Accept To Add As Friend!")
                return
            mycursor.execute('insert into requests (to_id, from_id) values (%s, %s);', [
                             int(send_id), id])

            mydb.commit()
            print("Friend Request Send!")

            break

        print("User Doesn't Exist!")


def accept_request(id):
    while True:
        print("Enter The User Id To Accept Request")
        choice = input()
        if choice.isnumeric():
            mycursor.execute(
                'select * from requests where to_id = %s and from_id = %s', [id, int(choice)])
            result = mycursor.fetchone()
            if not result:
                print("Request Not Found!")
                continue

            mycursor.execute('insert into friends (friend_one, friend_two) values (%s, %s)', [
                             int(choice), id])
            mycursor.execute('insert into friends (friend_one, friend_two) values (%s, %s)', [
                             id, int(choice)])
            mycursor.execute('delete from requests where to_id = %s and from_id = %s', [
                             id, int(choice)])
            mydb.commit()
            break

        print("Wrong User ID!")


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
                continue

            mycursor.execute('delete from requests where to_id = %s and from_id = %s', [
                             id, int(choice)])
            mydb.commit()
            break

        print("Wrong User ID!")

