import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project', buffered = True)

mycursor = mydb.cursor()

def exit_program():
    mycursor.close()
    mydb.close()
