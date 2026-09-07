##Revision
#Changes from my previous design: 
#Added 4 methods as neecessary functions 2 for compartments (Create, Delete), 2 for usernames (create, delete) and changed a few properties types to string 


"""
In UML: 
+ Public


- Private
    - Compartments : int
    - Files : string
    - Available : Boolean
    - Take : string                               
    - Username : string
    - User_passkey : string
    
    
"""

'''
Atrribute       Data Type       Visibility      Why?

Available       Boolean         Private         Because it is displaying wheather a file is available natively in the class
username        String          Private         Checks the username the user inputted to the username within the class
User_passkey    string          private         Checks user input to existing password
compartments    int             private         Only checks number of compartments within class
files           string          private         files the exist within the class

'''

UPDATED ULM
![UPDATED ULM](<Screenshot 2026-09-07 204355.png>)

PYTHON CODE
[pythoncode](<classImplementation.py>)

TEST RUN
![TEST](<Screenshot 2026-09-07 214907.png>)

OBJECT DIAGRAM
![OBJECT DIAGRAM](<Screenshot 2026-09-07 215815.png>)

ANALYSIS

### Why did you make your chosen attribute private? 
    Because it is the user login information if it were to be access by other people then it wouldnt keep their files safe
### Which method changes the state of your object? 
    The addfiles() this adds a files to the object making a
### How did your two objects demonstrate that instances are independent? 
    In the test i gave the two instances two different sets of inputs when checked again the objects showed the inputs seperately making them independent of each other
### What is the difference between your class diagram and your object diagram? 
    My class diagram shows the make up of the Class or blueprint of the object whilst the object diagram merely showed how the object differed from each other and the class


