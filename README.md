# Grocery-Management
Grocery Store Management Project Developed For MySql Training With Python

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


Update : 12th June, 2021

Added Email Verification While A User Registers.

Update : 13th June, 2021

Major Bug Fixes:
Added default_permission to users table so they can change permissions from there for friends
Fixed Multiple Screens Where User Could Not Go Back and Was stuck in a loob
Fixed Issues Where Menu Was Not Shown after a choice
Added Feature where two users can't have same email id
Added feature where a list should always have a name
and many more...

THIS IS A MAJOR MILESTONE WHERE BASIC PROJECT IS COMPLETED AND FROM HERE ADDITIONAL FUNCTIONALITIES WILL BE ADDED REGULARLY

Update  14th June 2021

Updated Database Model 
Created Database For Whole Grocery Store Instead Of Just Fruits
Removed Unnecessary Import Statements
Made Changes To Code According To Database Changes
Made A Category Section Where User Can View Items According To Their Categories


Update 15th June 2021

Added Phone Number Registration

Update 16th June 2021

Added Profile Page
Added Environment Variables For Sending Sms And Email Just For Security Reasons, May Host Online Securely Sometime Later
Added Feature Of Adding Phone Number If Registered Through Email And Vice Versa
Added Offers Sections, More Details In Upcoming Updates