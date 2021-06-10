import mysql.connector
import Requests,Permissions
mydb = mysql.connector.connect(host='localhost', user='user1', passwd='passwd', database='project')

mycursor = mydb.cursor()

def view_friends(id):
    mycursor.execute(
        'select * from friends where %s in (friend_one, friend_two)', [id])
    result = mycursor.fetchall()

    if not result:
        print("No Friends To Show!")
        return

    print("%-5s %-12s %-8s" % ('ID', 'NAME', "PERMISSION TO VIEW LISTS"))
    for res in result:
        if res[0] == id:

            mycursor.execute(
                'select user_name from users where user_id = %s', [res[1]])
            frnd = mycursor.fetchone()[0]
            print("%-5s %-12s %-8s" % (res[1], frnd, res[2]))


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
        print("3. Send A Friend Request")
        print("4. Change Friend Permission")
        print("5. Exit")
        
        while True:
            choice = input("Please Enter Your Choice!")
            if choice.isnumeric() and int(choice) in range(1,6):
                if int(choice) == 5:
                    return
                
                if int(choice) == 1:
                    view_friends(id)               
                
                if int(choice) == 2:
                    Requests.view_requests(id)
        
                if int(choice) == 3:
                    Requests.send_request(id)
                                    
                if int(choice) == 4:
                    Permissions.change_permission(id)
                
                break
            
            print("Wrong Choice!")
