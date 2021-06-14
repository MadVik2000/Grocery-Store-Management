import os
import db

def all_price(id):
    db.mycursor.execute('select list_name, list_price from lists where list_id = %s;', [id])
    price = db.mycursor.fetchone()
    
    print(f"Your List: {price[0]} contains items worth a total value of {price[1]}")
    
    input("Press Enter To Continue")
    os.system("cls")


def list_items_price(id):
    db.mycursor.execute('select li.quantity, i.item_name, li.item_price from list_items li join item i on li.item_id = i.item_id where li.list_id = %s;', [int(id)])
    prices = db.mycursor.fetchall()
    
    for index,price in enumerate(prices):
        print(f"{index + 1}. You have {price[0]} {price[1]} for a total price of {price[2]}.")
        
    input("Press Enter To Continue")
    os.system("cls")
