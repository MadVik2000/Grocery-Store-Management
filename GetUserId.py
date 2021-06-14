import db

def user_id(username):
    db.mycursor.execute('select user_id from users where user_name = %s', [username])
    
    return db.mycursor.fetchone()[0]