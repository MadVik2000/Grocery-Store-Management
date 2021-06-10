import mysql.connector
import Friends

mydb = mysql.connector.connect(host='localhost', user='user1', passwd='passwd', database='project')

mycursor = mydb.cursor()


def change_permission(id):
    while True:
        print("By Default, None Of Your Friends Can See You Lists Until You Grant Them Permission\n\n")
        print("1. See Friends")
        print("2. Change Permission For A Friend")
        print("3. Change Permission For All Friends")
        print("4. Exit")

        choice = input("Enter Your Choice!")

        if choice.isnumeric() and int(choice) in range(1, 5):
            if int(choice) == 4:
                return

            if int(choice) == 1:
                Friends.view_friends(id)

            if int(choice) == 2:
                while True:
                    print("Please Enter User Id Whose Permission You Want To Change")
                    frnd_id = input()
                    if Friends.check_friend(id, frnd_id):
                        break

                    print("Not Friends With The Given User Id")

                while True:
                    print("Press Y for Enable and N for Disable")
                    cho = input().lower()
                    if cho in ['y', 'n']:
                        mycursor.execute(
                            'update friends set permission = %s where friend_one = %s and friend_two = %s', [cho, id, frnd_id])
                        mydb.commit()
                        break

                    print("Wrong Choice!")

                continue

            if int(choice) == 3:
                while True:
                    print(
                        "Do you Want To Enable or Disable All Users To See Your Lists?")
                    print("Press Y for Enable and N for Disable")
                    cho = input().lower()
                    if cho in ['y', 'n']:
                        mycursor.execute(
                            'update friends set permission = %s where friend_one = %s', [cho, id])
                        mydb.commit()
                        break

                    print("Wrong Choice!")

                continue
        else:
            print("Wrong Choice!")

def fetch_permission(id, see_id):
    mycursor.execute('select permission from friends where friend_one = %s and friend_two = %s', [see_id, id])
    result = mycursor.fetchone()[0]
    
    return result