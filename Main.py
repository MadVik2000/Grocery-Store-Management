import CreateList, Fruits, CheckList, Friends
import Login
import Signup
import Password

if __name__ == "__main__":
    print("Welcome!")
    while True:
        print("1. Login")
        print("2. Signup")
        print("3. Forgot Password!")
        print("4. Exit")
        
        choice = input("Please Enter Your Choice!")
        if choice.isnumeric() and int(choice) in range(1, 5):

            if int(choice) == 4:
                break

            if int(choice) == 1:
                if Login.login():
                    while True:
                        print("1. Check Out The Fruits Available")
                        print("2. Create A New List")
                        print("3. Check Out An Old List")
                        print("4. Friends Section!")
                        print("5. Exit")

                        choice = input("Enter Your Choice")
                        if choice.isnumeric() and int(choice) in range(1, 6):

                            if int(choice) == 5:
                                break

                            if int(choice) == 1:
                                Fruits.show_fruits()
                                continue

                            if int(choice) == 2:
                                CreateList.create_list(int(id))
                                continue

                            if int(choice) == 3:
                                CheckList.check_list(int(id))
                                continue

                            if int(choice) == 4:
                                Friends.main(int(id))
                                continue
                        else:
                            print("Please Enter A Valid Choice")

            if int(choice) == 2:
                Signup.signup()
                continue

            if int(choice) == 3:
                Password.forgot_passwd()
                continue

        else:
            print("Wrong Choice!")
        
