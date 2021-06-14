import Categories
import ShowPrices
import os, time
import db

def create_list(id):
    while True:
        print("Please Enter The Name Of The List")
        name = input()
        
        if not name:
            print("List Needs To Have A Name!")
            time.sleep(1)
            os.system("cls")
            continue
        
        os.system("cls")
        break

    db.mycursor.execute('insert into lists(user_id, list_name) values (%s, %s);', [id, name])

    db.mydb.commit()
    while True:
        print("Want To Add Items To The List (Y/N)?")
        choice = input()
        os.system("cls")
        
        if choice.isalpha() and choice.lower() in ['y', 'n']:
            if choice.lower() == 'y':
                db.mycursor.execute('select max(list_id) from lists;')
                list_id = db.mycursor.fetchone()[0]
                enter_elem_list(list_id)

            else:
                print("Did Not Enter Element In List")

            break
        
        else:
            print("Please Enter Y or N only!")
            time.sleep(1)
            os.system("cls")


def enter_elem_list(id):

    db.mycursor.execute('select max(item_id) from items;')
    max_id = db.mycursor.fetchone()[0]

    while True:
        print("1. Show Categories")
        print("2. Show Items Related To A Category")
        print("3. Add An Item To The List")
        print("4. Show Total Price Of All Items In The List")
        print("5. Show Total Price For Every Item")
        print("6. Exit")
        choice = input("Please Enter Your Choice")
        os.system("cls")
        
        if choice.isnumeric() and int(choice) in range(1, 7):
            if int(choice) == 6:
                break

            if int(choice) == 1:
                Categories.show_category()
                continue
            
            if int(choice) == 2:
                Categories.show_items()
                continue

            if int(choice) == 3:

                while True:
                    id_choice = input("Please Enter Item Id Of The Item You Want To Purchase")
                    os.system("cls")
                    
                    if id_choice.isnumeric() and int(id_choice) in range(1, max_id+1):
                        
                        db.mycursor.execute('select item_price from items where item_id = %s', [int(id_choice)])
                        price = db.mycursor.fetchone()[0]

                        while True:

                            quantity = input("Enter The Quantity You Want To Enter")
                            os.system("cls")
                            
                            if quantity.isnumeric():
                                
                                if int(quantity) == 0:
                                    print("Try Adding Some Quantity!")
                                    continue

                                if int(quantity) > 20:
                                    print("Can't Add More Than 20 Units")
                                    time.sleep(1)
                                    os.system("cls")
                                    continue
                                
                                db.mycursor.execute('select * from list_items where list_id = %s and item_id = %s', [id, int(id_choice)])
                                result = db.mycursor.fetchone()
                                if not result:
                                   
                                    db.mycursor.execute('insert into list_items (list_id, item_id, quantity, item_price) values(%s, %s, %s, %s)', [
                                                    id, int(id_choice), int(quantity), price * int(quantity)])
                                    
                                    db.mydb.commit()
                                    break
                                
                                if result[3] + int(quantity) >20:
                                    print("Can't Add Quantity! Total Can't Be Bigger Than 20")
                                    time.sleep(1)
                                    os.system("cls")
                                    break
                                
                                db.mycursor.execute('update list_items set quantity = quantity + %s where list_id = %s and item_id = %s', [int(quantity), id, int(id_choice)])
                                db.mydb.commit()
                                
                                db.mycursor.execute('update list_items set item_price = quantity * %s where list_id = %s and item_id = %s', [price, id, int(id_choice)])
                                db.mydb.commit()
                                break

                            print("Incorrect Quantity!")
                            time.sleep(1)
                            os.system("cls")

                        print("Item Added To The List!")
                        time.sleep(1)
                        os.system("cls")
                        
                        db.mycursor.execute('select sum(item_price) from list_items where list_id = %s', [id])
                        total_price = db.mycursor.fetchone()[0]
                        
                        db.mycursor.execute('update lists set list_price = %s where list_id = %s', [total_price, id])
                        db.mydb.commit()
                        break

                    else:
                        print("Enter A Valid Item ID")
                        time.sleep(1)
                        os.system("cls")
                        break

                continue
            
            if int(choice) == 4:
                print("Showing Price For All Items")
                ShowPrices.all_price(id)
                continue
            
            if int(choice) == 5:
                
                db.mycursor.execute('select * from list_items where list_id = %s', [id])
                if not db.mycursor.fetchone():
                    print("No Items To Show In The List")
                    time.sleep(1)
                    os.system("cls")
                    continue
                    
                print("Showing Price For Each Item")
                ShowPrices.list_items_price(id)
                continue

            else:
                print("Please Enter A Valid Choice")
                time.sleep(1)
                os.system("cls")
                
        else:
            print("Wrong Choice")
            time.sleep(1)
            os.system('cls')
