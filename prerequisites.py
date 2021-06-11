#Please Execute Only Once

import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'user1', passwd = 'passwd', database = 'project')

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users(user_id INT AUTO_INCREMENT PRIMARY KEY,user_name VARCHAR(50) UNIQUE,email VARCHAR(50),passwd VARCHAR(64))")

mycursor.execute("CREATE TABLE fruits(fruit_id INT AUTO_INCREMENT PRIMARY KEY, fruit_name VARCHAR(50) UNIQUE, fruit_price FLOAT);")

mycursor.execute("CREATE TABLE lists(list_id INT AUTO_INCREMENT PRIMARY KEY,user_id INT,list_name VARCHAR(50),FOREIGN KEY(user_id)REFERENCES users(user_id));")

mycursor.execute("CREATE TABLE list_items(items_id INT AUTO_INCREMENT PRIMARY KEY, list_id INT REFERENCES lists(list_id), fruit_id INT REFERENCES fruits(fruit_id), quantity INT);")

mycursor.execute(
    
    "CREATE TABLE requests(request_id INT AUTO_INCREMENT PRIMARY KEY, to_id INT references users(user_id),from_id INT references users(user_id));")

mycursor.execute(
    "CREATE TABLE friends(friends_id INT AUTO_INCREMENT PRIMARY KEY, friend_one INT REFERENCES users(user_id),friend_two INT REFERENCES users(user_id),permission ENUM('y', 'n') DEFAULT 'n');")

myquery = "insert into fruits(fruit_name,fruit_price) values (%s, %s)"
fruit_list = [('apple',30),('banana',50),('grapes', 60),('guava',40),('litchi',70),('mango',120),
              ('orange',50),('papapya',60),('pear',30),('pineapple',80),('pomegranate',70),
              ('watermelon',80)]

mycursor.executemany(myquery, fruit_list)

mydb.commit()
