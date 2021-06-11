import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', user='user1', passwd='passwd', database='project')
mycursor = mydb.cursor()

def user_id(username):
    mycursor.execute('select user_id from users where user_name = %s', [username])
    
    return mycursor.fetchone()[0]