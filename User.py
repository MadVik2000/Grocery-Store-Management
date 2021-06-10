import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="user1", passwd="passwd", database='project')

mycursor = mydb.cursor()


def check_user(id):
    mycursor.execute('select user_id from users where user_id = %s;', [id])

    if mycursor.fetchone():
        return True

    else:
        return False


def new_user():
    print("Please Enter Your Name")
    name = input()
    mycursor.execute('insert into users(user_name) values (%s);', [name])

    mydb.commit()

    mycursor.execute('select max(user_id) from users;')
    id = mycursor.fetchone()[0]

    print(f"Your Assigned Id is {id}")
    return id
