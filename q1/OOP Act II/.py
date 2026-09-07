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

class YourClass: 
    def __init__(Safe, value1, value2, value3): 
         

