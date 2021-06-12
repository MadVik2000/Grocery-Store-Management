import mysql.connector,Fruits
import ShowPrices
import os, time

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()

def create_list(id):
    print("Please Enter The Name Of The List")
    name = input()
    os.system("cls")

    mycursor.execute('insert into lists(user_id, list_name) values (%s, %s);', [id, name])

    mydb.commit()
    while True:
        print("Want To Add Items To The List (Y/N)?")
        choice = input()
        os.system("cls")
        
        if choice.isalpha() and choice.lower() in ['y', 'n']:
            if choice.lower() == 'y':
                mycursor.execute('select max(list_id) from lists;')
                list_id = mycursor.fetchone()[0]
                enter_elem_list(list_id)

            else:
                print("Did Not Enter Element In List")

            break
        
        else:
            print("Please Enter Y or N only!")
            time.sleep(1)
            os.system("cls")


def enter_elem_list(id):

    mycursor.execute('select max(fruit_id) from fruits;')
    max_id = mycursor.fetchone()[0]

    while True:
        print("1. Show Fruits")
        print("2. Add A Fruit To The List")
        print("3. Show Total Price Of All Items In The List")
        print("4. Show Total Price For Every Item")
        print("5. Exit")
        choice = input("Please Enter Your Choice")
        os.system("cls")
        
        if choice.isnumeric and int(choice) in range(1, 6):
            if int(choice) == 5:
                break

            if int(choice) == 1:
                Fruits.show_fruits()
                continue

            if int(choice) == 2:

                while True:
                    id_choice = input("Please Enter Fruit Id Of The Fruit You Want To Purchase")
                    os.system("cls")
                    
                    if id_choice.isnumeric() and int(id_choice) in range(1, max_id+1):
                        
                        mycursor.execute('select fruit_price from fruits where fruit_id = %s', [int(id_choice)])
                        price = mycursor.fetchone()[0]

                        while True:

                            quantity = input("Enter The Quantity You Want To Enter")
                            os.system("cls")
                            
                            if quantity.isnumeric():

                                if int(quantity) > 20:
                                    print("Can't Add More Than 20 Units")
                                    time.sleep(1)
                                    os.system("cls")
                                    continue
                                
                                mycursor.execute('select * from list_items where list_id = %s and fruit_id = %s', [id, int(id_choice)])
                                result = mycursor.fetchone()
                                if not result:
                                   
                                    mycursor.execute('insert into list_items (list_id, fruit_id, quantity, item_price) values(%s, %s, %s, %s)', [
                                                    id, int(id_choice), int(quantity), price * int(quantity)])
                                    
                                    mydb.commit()
                                    break
                                
                                if result[3] + int(quantity) >20:
                                    print("Can't Add Quantity! Total Can't Be Bigger Than 20")
                                    time.sleep(1)
                                    os.system("cls")
                                    break
                                
                                mycursor.execute('update list_items set quantity = quantity + %s where list_id = %s and fruit_id = %s', [int(quantity), id, int(id_choice)])
                                mydb.commit()
                                
                                mycursor.execute('update list_items set item_price = quantity * %s where list_id = %s and fruit_id = %s', [price, id, int(id_choice)])
                                mydb.commit()
                                break

                            print("Incorrect Quantity!")
                            time.sleep(1)
                            os.system("cls")

                        print("Item Added To The List!")
                        time.sleep(1)
                        os.system("cls")
                        
                        mycursor.execute('select sum(item_price) from list_items where list_id = %s', [id])
                        total_price = mycursor.fetchone()[0]
                        
                        mycursor.execute('update lists set list_price = %s where list_id = %s', [total_price, id])
                        mydb.commit()
                        break

                    else:
                        print("Enter A Valid Fruit ID")
                        time.sleep(1)
                        os.system("cls")

                continue
            
            if int(choice) == 3:
                print("Showing Price For All Items")
                ShowPrices.all_price(id)
                continue
            
            if int(choice) == 4:
                print("Showing Price For Each Item")
                ShowPrices.list_items_price(id)
                continue

            else:
                print("Please Enter A Valid Choice")
                time.sleep(1)
                os.system("cls")
