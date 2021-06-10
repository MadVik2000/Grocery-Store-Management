import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()

def print_all_lists(id):
    
    mycursor.execute('select list_id, list_name from lists where user_id = %s',[id])
    result = mycursor.fetchall()
    
    if not result:
        print("No Lists Found!")
        return
    
    print("%-8s %-12s" % ('List Id', 'List Name'))
    
    for res in result:
        print("%-8s %-12s" %(res[0], res[1]))
        
def print_one_list(id, list_id):
    
    mycursor.execute('select u.user_id, li.fruit_id, f.fruit_name, li.quantity from list_items as li join fruits f on li.fruit_id = f.fruit_id join lists l on li.list_id = l.list_id join users u on l.user_id = u.user_id where li.list_id = %s and u.user_id = %s', [list_id, id])
    result = mycursor.fetchall()
    
    if not result:
        print("No List Found with the Particular Id")
        return

    print("%-8s %-8s %-12s %-8s" % ('User Id', 'Fruit Id', 'Fruit Name', 'Quantity'))

    for res in result:
        print("%-8s %-8s %-12s %-8s" % (res[0], res[1], res[2], res[3]))
    
