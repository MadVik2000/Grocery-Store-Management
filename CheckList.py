from Permissions import fetch_permission
from Friends import check_friend, check_friend_list, view_friends
from User import check_user_id
import PrintLists
import os, time
import db

def list_present(list_id):
    db.mycursor.execute('select * from lists where list_id = %s', [list_id])
    if db.mycursor.fetchone():
        return True
    
    return False
    

def check_list(id):
    
    while True:
        print("1. Check List Names")
        print("2. Check Friend's Lists")
        print("3. Check A List Items")
        print("4. Exit")

        choice = input("Please Enter Your Choice!")
        os.system("cls")
        
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
                    os.system("cls")
                    
                    if cho.isnumeric() and int(cho) in range(1,5):
                        
                        if int(cho) == 4:
                            break
                        
                        if int(cho) == 3:
                            view_friends(id)
                            continue
                        
                        if int(cho) in [1,2]:
                            print("Enter Friend ID")
                            frnd_id = input()
                            os.system("cls")
                            
                            if int(frnd_id) == id:
                                print("Can't Check Own Records In Friends Section!")
                                time.sleep(1)
                                os.system('cls')
                                continue
                            
                            if check_user_id(int(frnd_id)):
                                
                                if check_friend(id, int(frnd_id)):
                                    
                                    perm = fetch_permission(id, int(frnd_id))
                                    if perm == 'n':
                                        print("User Has Disabled Viewing His/Her Profile Lists")
                                        time.sleep(1)
                                        os.system("cls")
                                        
                                        continue
                                        
                                    else:
                                        if int(cho) == 2:
                                            PrintLists.print_all_lists(int(frnd_id))
                                            continue
                                        
                                        elif int(cho) == 1:
                                            print("Enter The List Id Of The List You Want To See")
                                            list_id = input()
                                            os.system("cls")
                                            
                                            if check_friend_list(int(frnd_id), int(list_id)):
                                            
                                                if list_id.isnumeric():
                                                    if list_present(int(list_id)):
                                                        PrintLists.print_one_list(int(frnd_id), int(list_id))
                                                        continue
                                                    
                                                    print("List Not Available!")
                                                    continue
                                                
                                            else:
                                                
                                                if not list_present(int(list_id)):
                                                    print("List Not Available!")
                                                    time.sleep(1)
                                                    os.system("cls")
                                                    continue
                                                
                                                print("This List Id Doesn't Belongs To Your Friend!")
                                                time.sleep(1)
                                                os.system("cls")
                                                continue
                                
                                else:
                                    print("You Are Not Friends With This User")
                                    time.sleep(1)
                                    os.system("cls")
                                    
                                    continue
                                
                            else:
                                print("User Doesn't Exists!")
                                time.sleep(1)
                                os.system("cls")
                                
                                continue
                        
                    else:
                        print("Wrong Choice!")
                        time.sleep(1)
                        os.system("cls")
                            
                

            if int(choice) == 3:
                while True:
                    list_id = input("Please Enter List_Id You Want To See")
                    os.system("cls")
                    
                    if list_id.isnumeric():
                        if list_present(int(list_id)):
                            PrintLists.print_one_list(id, list_id)
                            break
                        
                        print("List Not Available!")
                        time.sleep(1)
                        os.system("cls")
                        break

                    print("Wrong List Id")
                    time.sleep(1)
                    os.system("cls")

                continue
            
        else:
            print("Wrong Choice!")
            time.sleep(1)
            os.system("cls")
