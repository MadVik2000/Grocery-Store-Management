import mysql.connector
import os

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()

def show_fruits():
    mycursor.execute('select * from fruits;')
    result = mycursor.fetchall()

    print("%-8s %-12s %-12s" % ('Fruit ID', 'Fruit Name', 'Fruit Price'))
    for res in result:
        print('%-8s %-12s %-12s' % (res[0], res[1], res[2]))
        
    
    input("Press Enter To Continue")
    os.system("cls")
