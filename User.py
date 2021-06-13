import mysql.connector
import re
import db
def check_user_id(id):
    db.mycursor.execute('select user_id from users where user_id = %s;', [id])

    if db.mycursor.fetchone():
        return True

    else:
        return False

def check_user(username):
    db.mycursor.execute(
        'select user_id from users where user_name = %s', [username])
    result = db.mycursor.fetchone()
    if result:
        return True

    return False


def check_pass(username, passwd):
    db.mycursor.execute(
        'select passwd from users where user_name = %s', [username])
    result = db.mycursor.fetchone()[0]
    if result == passwd:
        return True

    return False


def check_mail(mail_id):

    pattern = r'[a-zA-Z0-9.]+@[a-zA-Z]+\.(com|edu|net|org)'
    if re.match(pattern, mail_id):
        
        db.mycursor.execute('select email from users where email = %s', [mail_id])
        if db.mycursor.fetchone():
            print("Email Already Exists!")
            return False
        
        return True
    
    print("Email Standards Not Met")
    return False
