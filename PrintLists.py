import os,time
import db

def print_all_lists(id):
    
    db.mycursor.execute('select list_id, list_name, list_price from lists where user_id = %s',[id])
    result = db.mycursor.fetchall()
    
    if not result:
        print("No Lists Found!")
        time.sleep(1)
        os.system("cls")
        return
    
    print("%-20s %-20s %-20s" % ('List Id', 'List Name', 'List Price'))
    
    for res in result:
        print("%-20s %-20s %-20s" %(res[0], res[1], res[2]))
        
    input("Press Enter To Continue")
    os.system("cls")
        
def print_one_list(id, list_id):
    
    db.mycursor.execute('select i.item_name, li.quantity, li.item_price from list_items li join items i on li.item_id = i.item__id join lists l on li.list_id = l.list_id where li.list_id = %s and l.user_id = %s', [int(list_id), int(id)])
    
    result = db.mycursor.fetchall()
    
    if not result:
        print("List Contains No Items!")
        time.sleep(1)
        os.system("cls")
        return

    print("%-12s %-12s %-12s" % ('Item Name', 'Quantity', 'Price'))

    for res in result:
        print("%-12s %-12s %-12s" % (res[0], res[1], res[2]))
        
    input("Press Enter To Continue")
    os.system("cls")
    
