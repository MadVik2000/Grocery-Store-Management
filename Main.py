import User, CreateList, Fruits, CheckList, Friends


if __name__ == "__main__":
    print("Welcome!")
    while True:
        print("Enter Your User Id Please! Enter 0 if no user id is assigned")
        id = input()
        if id.isnumeric():
            if int(id) == 0:
                id = User.new_user()
                break
            
            if User.check_user(int(id)):
                print("User Found!")
                break
            
            print("User Id Not Found!")
            
        print("Wrong User Id Format!")
        
    while True:    
        print("1. Check Out The Fruits Available")
        print("2. Create A New List")
        print("3. Check Out An Old List")
        print("4. Friends Section!")
        print("5. Exit")
        
        choice = input("Enter Your Choice")
        if choice.isnumeric() and int(choice) in range(1,6):
            
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
            
            if int(choice) ==4:
                Friends.main(int(id))
                continue
        else:        
            print("Please Enter A Valid Choice")
