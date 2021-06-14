import os, time
import db

def show_category():
    db.mycursor.execute('select * from categories;')
    result = db.mycursor.fetchall()
    
    print("%-15s %-20s" % ('Category ID', 'Category Name'))
    for res in result:
        print('%-15s %-20s' % (res[0], res[1]))
    
    while True:    
        print("\nWant To See Items In A Specific Category?")
        cho = input("Press Y for Yes and N for No\n")
        
        if cho.lower() in ['y', 'n']:
            if cho.lower() == 'y':
                show_items()
            
            os.system('cls')   
            return
            
        else:
            print("Please Enter Either Yes Or No (y/n).")
            time.sleep(1)
            os.system('cls')
            continue
        

def show_items():
    print("Enter Category Id To See Items In That Category!")
    choice = input()
    os.system('cls')
    if choice.isnumeric():
        db.mycursor.execute('select * from categories where category_id = %s', [int(choice)])
        if not db.mycursor.fetchone():
            print("Category Id Doesn't Exists!")
            time.sleep(1)
            os.system('cls')
            return

        db.mycursor.execute('select item_id, item_name, item_price from items where category_id = %s', [int(choice)])
        items = db.mycursor.fetchall()
        if not items:
            print("No Items To Show In This Category")
            time.sleep(1)
            os.system('cls')
            return

        print("%-8s %-40s %-12s" % ('Item ID', 'Item Name', 'Item Price'))
        for item in items:
            print('%-8s %-40s %-12s' % (item[0], item[1], item[2]))
            
        input("Press Enter To Continue")
        os.system("cls")
        return

    print("Wrong Choice!")
    time.sleep(1)
    os.system('cls')
    return

