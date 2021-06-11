# List-Management
List Management Project Developed For MySql Training With Python

I made this list management project to understand how python and mysql works together and to get a better understanding of how we query databases in mysql
through python mysql connector.

We need to create a user named 'user1' with a password 'passwd' on the local machine.
Furthermore, we need to create a database named project.
Also, we need to grant the user all privileges on this database.

Now , before we start the program, we need to run the prerequisites.py file in order to create all the tables needed for this project
The Code can be run through main.py file

We can create a user, add a list for that user, see that list whenever we want.

There is also friendship system added in this project where we can send requests to other users and connect with them as friends

Friends have the ability to see each other lists.
By default, list sharing is disabled but can be changed within navigating the code execution.
Only if a friend has permission from other friend, then that friend can see his/ her friends lists.



Update : 11th June, 2021

Added Login System Instead of user just registering them into the database.
User can sign up where they'll be asked their email id and password to login afterwards.
Passwords are stored securely after encrypting them using sha256 hashing technique
If a user forgets passwords they can request to change it. A code will be send to mail id given by the user to verify a code.
After Code Verification, User Can change his/ her password