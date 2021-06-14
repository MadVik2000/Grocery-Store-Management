import CreateList, Categories, CheckList, Friends
import Login
import Signup
import Password
import GetUserId
import os, time

if __name__ == "__main__":
    os.system('cls')
    print("Welcome To The List Management System!")
    while True:
        print("1. Login")
        print("2. Signup")
        print("3. Forgot Password!")
        print("4. Exit")
        
        choice = input("Please Enter Your Choice!")
        if choice.isnumeric() and int(choice) in range(1, 5):
            
            os.system("cls")

            if int(choice) == 4:
                break

            if int(choice) == 1:
                print("Please Enter Your Username")
                    
                username = input()
                os.system("cls")
                
                if Login.login(username):
                        
                    user_id = int(GetUserId.user_id(username))
                    while True:
                        print("1. Check Out The Categories Available")
                        print("2. Create A New List")
                        print("3. Check Out An Old List")
                        print("4. Friends Section!")
                        print("5. Exit")

                        cho = input("Enter Your Choice")
                        os.system('cls')
                        if cho.isnumeric() and int(cho) in range(1, 6):
                            
                            os.system("cls")

                            if int(cho) == 5:
                                break

                            if int(cho) == 1:
                                Categories.show_category()
                                continue

                            if int(cho) == 2:
                                CreateList.create_list(user_id)
                                continue

                            if int(cho) == 3:
                                CheckList.check_list(user_id)
                                continue

                            if int(cho) == 4:
                                Friends.main(user_id)
                                continue
                            
                        else:
                            print("Please Enter A Valid Choice")
                            time.sleep(1)
                            os.system("cls")

            if int(choice) == 2:
                Signup.signup()
                continue

            if int(choice) == 3:
                Password.forgot_passwd()
                continue

        else:
            print("Wrong Choice!")
            time.sleep(1)
            os.system("cls")
        
