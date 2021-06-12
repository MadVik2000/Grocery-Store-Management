import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()

def print_all_lists(id):
    
    mycursor.execute('select list_id, list_name, list_price from lists where user_id = %s',[id])
    result = mycursor.fetchall()
    
    if not result:
        print("No Lists Found!")
        return
    
    print("%-20s %-20s %-20s" % ('List Id', 'List Name', 'List Price'))
    
    for res in result:
        print("%-20s %-20s %-20s" %(res[0], res[1], res[2]))
        
def print_one_list(id, list_id):
    
    mycursor.execute('select f.fruit_name, li.quantity, li.item_price from list_items li join fruits f on li.fruit_id = f.fruit_id join lists l on li.list_id = l.list_id join users u on l.user_id = u.user_id where li.list_id = %s and u.user_id = %s', [list_id, id])
    
    result = mycursor.fetchall()
    
    if not result:
        print("No List Found with the Particular Id")
        return

    print("%-12s %-12s %-12s" % ('Fruit Name', 'Quantity', 'Price'))

    for res in result:
        print("%-12s %-12s %-12s" % (res[0], res[1], res[2]))
    
