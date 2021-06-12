import mysql.connector
import os

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()

def all_price(id):
    mycursor.execute('Select list_id, list_name, list_price from lists where list_id = %s', [id])
    price = mycursor.fetchone()
    
    print(f"List With Id Number: {price[0]} and name: {price[1]} is priced at {price[2]}")
    
    input("Press Enter To Continue")
    os.system("cls")


def list_items_price(id):
    mycursor.execute('Select li.quantity, f.fruit_name, li.item_price from list_items li join fruits f on li.fruit_id = f.fruit_id where li.list_id = %s', [id])
    prices = mycursor.fetchall()
    
    for index,price in enumerate(prices):
        print(f"{index + 1}. You have {price[0]} {price[1]} for a total price of {price[2]}.")
        
    input("Press Enter To Continue")
    os.system("cls")
