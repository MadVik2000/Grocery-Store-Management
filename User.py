import mysql.connector
import re

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()


def check_user_id(id):
    mycursor.execute('select user_id from users where user_id = %s;', [id])

    if mycursor.fetchone():
        return True

    else:
        return False

def check_user(username):
    mycursor.execute(
        'select user_id from users where user_name = %s', [username])
    result = mycursor.fetchone()
    if result:
        return True

    return False


def check_pass(username, passwd):
    mycursor.execute(
        'select passwd from users where user_name = %s', [username])
    result = mycursor.fetchone()[0]
    if result == passwd:
        return True

    return False


def check_mail(mail_id):

    pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org)'
    if re.match(pattern, mail_id):
        return True

    return False
