#Please Execute Only Once

import db
import Items

db.mycursor.execute(
    "CREATE TABLE users(user_id INT AUTO_INCREMENT PRIMARY KEY,user_name VARCHAR(50) UNIQUE,email VARCHAR(50) UNIQUE,passwd VARCHAR(64), default_permission ENUM('y', 'n') DEFAULT 'n');")

db.mycursor.execute("CREATE TABLE categories(category_id INT AUTO_INCREMENT PRIMARY KEY, category_name VARCHAR(50) UNIQUE);")

db.mycursor.execute("CREATE TABLE items(item_id INT AUTO_INCREMENT PRIMARY KEY, category_id INT REFERENCES categories(category_id), item_name VARCHAR(50), item_price FLOAT);")

db.mycursor.execute("CREATE TABLE lists(list_id INT AUTO_INCREMENT PRIMARY KEY,user_id INT,list_name VARCHAR(50) NOT NULL,FOREIGN KEY(user_id)REFERENCES users(user_id), list_price INT DEFAULT 0);")

db.mycursor.execute("CREATE TABLE list_items(list_items_id INT AUTO_INCREMENT PRIMARY KEY, list_id INT REFERENCES lists(list_id), item_id INT REFERENCES items(item_id), quantity INT, item_price INT);")

db.mycursor.execute(
    
    "CREATE TABLE requests(request_id INT AUTO_INCREMENT PRIMARY KEY, to_id INT references users(user_id),from_id INT references users(user_id));")

db.mycursor.execute(
    "CREATE TABLE friends(friends_id INT AUTO_INCREMENT PRIMARY KEY, friend_one INT REFERENCES users(user_id),friend_two INT REFERENCES users(user_id),permission ENUM('y', 'n'));")

for item in Items.ITEMS:
    db.mycursor.execute('insert into categories (category_name) value(%s)', [item])
    

    
myquery ='insert into items (category_id, item_name, item_price) values (%s, %s, %s)'

db.mycursor.executemany(myquery,Items.FRUITS)

db.mycursor.executemany(myquery, Items.RICEGRAINPULSES)

db.mycursor.executemany(myquery, Items.SALTSUGARSPICES)

db.mycursor.executemany(myquery, Items.FLOURSEMOLINAPROCESSEDGRAINS)

db.mycursor.executemany(myquery, Items.GROUNDSPICES)

db.mycursor.executemany(myquery, Items.DAIRYFROZENFOOD)

db.mycursor.executemany(myquery, Items.BREADPOULTRYCEREALSSNACKS)

db.mycursor.executemany(myquery, Items.BEVERAGES)

db.mycursor.executemany(myquery, Items.ACCOMPANIMENTS)

db.mycursor.executemany(myquery,Items.SWEETSDRYFRUITS)

db.mycursor.executemany(myquery,Items.BAKINGDESSERTPREPERATION)

db.mycursor.executemany(myquery, Items.OILGHEE)
    
db.mydb.commit()
