from User import check_user_id
import Friends
import os,time
import db


def change_permission(id):
    while True:
        print("By Default, None Of Your Friends Can See You Lists Until You Grant Them Permission\n\n")
        print("1. See Friends")
        print("2. Change Permission For A Friend")
        print("3. Change Permission For All Friends")
        print("4. Exit")

        choice = input("Enter Your Choice!")
        os.system("cls")

        if choice.isnumeric() and int(choice) in range(1, 5):
            if int(choice) == 4:
                return

            if int(choice) == 1:
                Friends.view_friends(id)
                continue

            if int(choice) == 2:
                while True:
                    print("Please Enter User Id Whose Permission You Want To Change")
                    frnd_id = input()
                    os.system("cls")
                    
                    if not check_user_id(int(frnd_id)):
                        print("No User Exists With That ID")
                        time.sleep(1)
                        os.system('cls')
                        return
                    
                    if Friends.check_friend(id, frnd_id):
                        break

                    print("Not Friends With The Given User Id")
                    time.sleep(1)
                    os.system("cls")
                    return

                while True:
                    print("Press Y for Enable and N for Disable")
                    cho = input().lower()
                    os.system('cls')
                    
                    if cho in ['y', 'n']:
                        db.mycursor.execute('update friends set permission = %s where friend_one = %s and friend_two = %s', [cho, id, frnd_id])
                        
                        print("Permission Updated!")
                        time.sleep(1)
                        os.system("cls")
                        
                        break

                    print("Wrong Choice!")
                    time.sleep(1)
                    os.system("cls")

                continue

            if int(choice) == 3:
                while True:
                    print("Do you Want To Enable or Disable All Users To See Your Lists?")
                    print("Press Y for Enable and N for Disable")
                    cho = input().lower()
                    os.system("cls")
                    
                    if cho in ['y', 'n']:
                        db.mycursor.execute('update friends set permission = %s where friend_one = %s', [cho, id])
                        
                        
                        db.mycursor.execute('update users set default_permission = %s where user_id = %s', [cho, id])
                        
                        print("Permissions Updated Successfully!")
                        time.sleep(1)
                        os.system("cls")
                        
                        break

                    print("Wrong Choice!")
                    time.sleep(1)
                    os.system("cls")

                continue
        else:
            print("Wrong Choice!")
            time.sleep(1)
            os.system("cls")

def fetch_permission(id, see_id):
    db.mycursor.execute('select permission from friends where friend_one = %s and friend_two = %s', [see_id, id])
    result = db.mycursor.fetchone()[0]
    
    return result
