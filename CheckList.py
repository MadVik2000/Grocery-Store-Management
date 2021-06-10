from Permissions import fetch_permission
from Friends import check_friend, view_friends
from User import check_user
import mysql.connector, PrintLists

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()


def check_list(id):

    mycursor.execute('select max(list_id) from lists')
    max_id = mycursor.fetchone()[0]

    while True:
        print("1. Check List Names")
        print("2. Check Friend's Lists")
        print("3. Check A List Items")
        print("4. Exit")

        choice = input("Please Enter Your Choice!")
        if choice.isnumeric() and int(choice) in range(1, 5):
            if int(choice) == 4:
                break

            if int(choice) == 1:
                PrintLists.print_all_lists(id)
                continue
            
            if int(choice) == 2:
                while True:
                    print("1. Check Friend's Particular List")
                    print("2. Check All Lists Related To A Friend")
                    print("3. See All Friends")
                    print("4. Exit")
                    cho = input()
                    if cho.isnumeric() and int(cho) in range(1,5):
                        
                        if int(cho) == 4:
                            break
                        
                        if int(cho) == 3:
                            view_friends(id)
                            continue
                        
                        if int(cho) in [1,2]:
                            print("Enter Friend ID")
                            frnd_id = input()
                            if check_user(int(frnd_id)):
                                
                                if check_friend(id, int(frnd_id)):
                                    
                                    perm = fetch_permission(id, int(frnd_id))
                                    if perm == 'n':
                                        print("User Has Disabled Viewing His/Her Profile Lists")
                                        continue
                                        
                                    else:
                                        if int(cho) == 2:
                                            PrintLists.print_all_lists(int(frnd_id))
                                            continue
                                        
                                        elif int(cho) == 1:
                                            print("Enter The List Id Of The List You Want To See")
                                            list_id = input()
                                            if list_id.isnumeric() and int(list_id) in range(1, max_id+1):
                                                PrintLists.print_one_list(int(frnd_id), int(list_id))
                                                continue
                                
                                else:
                                    print("You Are Not Friends With This User")
                                    continue
                                
                            else:
                                print("User Doesn't Exists!")
                                continue
                        
                    else:
                        print("Wrong Choice!")
                            
                

            if int(choice) == 3:
                while True:
                    list_id = input("Please Enter List_Id You Want To See")
                    if list_id.isnumeric() and int(list_id) in range(1, max_id+1):
                        PrintLists.print_one_list(id, list_id)
                        break

                    print("Wrong List Id")

                continue
            
        else:
            print("Wrong Choice!")
