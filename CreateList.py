import mysql.connector,Fruits

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()

def create_list(id):
    print("Please Enter The Name Of The List")
    name = input()

    mycursor.execute(
        'insert into lists(user_id, list_name) values (%s, %s);', [id, name])

    mydb.commit()
    while True:
        print("Want To Add Items To The List (Y/N)?")
        choice = input()
        if choice.isalpha() and choice.lower() in ['y', 'n']:
            if choice.lower() == 'y':
                mycursor.execute('select max(list_id) from lists;')
                list_id = mycursor.fetchone()[0]
                enter_elem_list(list_id)

            else:
                print("Did Not Enter Element In List")

            break


def enter_elem_list(id):

    mycursor.execute('select max(fruit_id) from fruits;')
    max_id = mycursor.fetchone()[0]

    while True:
        print("1. Show Fruits")
        print("2. Add A Fruit To The List")
        print("3. Exit")
        choice = input("Please Enter Your Choice")
        if choice.isnumeric and int(choice) in range(1, 4):
            if int(choice) == 3:
                break

            if int(choice) == 1:
                Fruits.show_fruits()
                continue

            if int(choice) == 2:

                while True:
                    id_choice = input(
                        "Please Enter Fruit Id Of The Fruit You Want To Purchase")
                    if id_choice.isnumeric() and int(id_choice) in range(1, max_id+1):

                        while True:

                            quantity = input(
                                "Enter The Quantity You Want To Enter")
                            if quantity.isnumeric():

                                if int(quantity) > 20:
                                    print("Can't Add More Than 20 Units")
                                    continue
                                
                                mycursor.execute('select * from list_items where list_id = %s and fruit_id = %s', [id, int(id_choice)])
                                result = mycursor.fetchone()
                                if not result:

                                    mycursor.execute('insert into list_items values(%s, %s, %s)', [
                                                    id, int(id_choice), int(quantity)])
                                    mydb.commit()
                                    break
                                
                                if result[2] + int(quantity) >20:
                                    print("Can't Add Quantity! Total Can't Be Bigger Than 20")
                                    break
                                
                                mycursor.execute('update list_items set quantity = quantity + %s where list_id = %s and fruit_id = %s', [int(quantity), id, int(id_choice)])
                                mydb.commit()
                                break

                            print("Incorrect Quantity!")

                        print("Item Added To The List!")
                        break

                    else:
                        print("Enter A Valid Fruit ID")

                continue

            else:
                print("Please Enter A Valid Choice")
