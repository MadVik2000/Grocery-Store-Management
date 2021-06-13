import mysql.connector
import os
import db

def show_fruits():
    db.mycursor.execute('select * from fruits;')
    result = db.mycursor.fetchall()

    print("%-8s %-12s %-12s" % ('Fruit ID', 'Fruit Name', 'Fruit Price'))
    for res in result:
        print('%-8s %-12s %-12s' % (res[0], res[1], res[2]))
        
    
    input("Press Enter To Continue")
    os.system("cls")
