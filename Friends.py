import mysql.connector
import Requests,Permissions
import os, time

mydb = mysql.connector.connect(host='localhost', user='user1', passwd='passwd', database='project')
mycursor = mydb.cursor()

def view_friends(id):
    mycursor.execute(
        'select * from friends where friend_one = %s', [id])
    result = mycursor.fetchall()

    if not result:
        print("No Friends To Show!")
        time.sleep(1)
        os.system("cls")
        return

    print("%-5s %-12s %-8s" % ('ID', 'NAME', "PERMISSION TO VIEW LISTS"))
    for res in result:
        mycursor.execute('select user_name from users where user_id = %s', [res[2]])
        frnd = mycursor.fetchone()[0]
        print("%-5s %-12s %-8s" % (res[2], frnd, res[3]))
        
    input("Press Enter To Continue")
    os.system("cls")


def check_friend(id, frnd_id):
    mycursor.execute(
        'select * from friends where friend_one = %s and friend_two = %s', [id, frnd_id])

    result = mycursor.fetchone()
    if not result:
        return False

    else:
        return True

def main(id):
    while True:
        print("1. Show Current Friends")
        print("2. View Friend Requests")
        print("3. Approve/Disapprove a Friend Request")
        print("4. Send A Friend Request")
        print("5. Change Friend Permission")
        print("6. Exit")
        
        while True:
            choice = input("Please Enter Your Choice!")
            os.system("cls")
            
            if choice.isnumeric() and int(choice) in range(1,7):
                if int(choice) == 6:
                    return
                
                if int(choice) == 1:
                    view_friends(id)
                    continue               
                
                if int(choice) == 2:
                    Requests.view_requests(id)
                    continue
                    
                if int(choice) == 3:
                    Requests.request_approval(id)
                    continue
        
                if int(choice) == 4:
                    Requests.send_request(id)
                    continue
                                    
                if int(choice) == 5:
                    Permissions.change_permission(id)
                    continue
                
                break
            
            print("Wrong Choice!")
            time.sleep(1)
            os.system("cls")
            
