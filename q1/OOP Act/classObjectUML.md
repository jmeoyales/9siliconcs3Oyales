# Step 1

Choose one real-world context that interests you. You may also choose another appropriate context. Examples: 

● School library 
● Science laboratory 
●Computer laboratory
●School canteen 
●Classroom 
● Sports 
● Transportation 
● School club 
● School event 
● Inventory 
● Game 
● Music 
● Personal productivity 

            Choice:
                A digital safe


# Step 2

Choose one important object or concept from your selected context. 
Examples: 
Context         Possible Class

Library         Book
Canteen         MenuItem
Laboratory      Equipment
Sports          Athlete
Transportation  Vehicle
Game            Character


                Object chosen is files


# Step 3

Identify at least four properties that describe your class. 
For each property specify: 

● Property name 
● Data type 
● Short description 

You may use simple data types such as: string, int, double, boolean 
Example 
If the class were Book: 

Property        Data Type       Description

title           string          Title of the book
author          string          Name of the author
pages           int             Number of pages
available       boolean         Indicates whether the book is available

Username        string          Asks for the users username
User passkey    string          Asks for their pass key to acess the safe
compartments    int             Displays all compartments
files           int             Displays all files in a compartment
Available       boolean         Displays all available files to take or add
Take            int             Allows to take a file from the safe
Add             int             Allows to add a file to the safe


# Step 4

Identify at least three methods that your class should be able to perform. For each method write a short description as to what the method does. A method represents an action or behavior. 
Method                                              Description

| Addfiles() |                                      Its function is to add a file upon the user request
| Addfiles(files : int) |                           

| Movefiles() |                                     Its function is to move a file to a compartment that the user picks
| Movefiles(files : int) |                          

| Access_safe() |                                   Its function is to allow the user to access the safe upon entering their 
| Access_safe(User passkey : string) |              passkey             

| Checkuser() |                                     Checks The users user name to match to a passkey
| Checkuser(Username : string) |                    

| Checkfiles() |                                    Displays all files and their state as available or not
| Checkfiles(Available : boolean) |                 

| Takefiles() |                                     Allows the user to take a file or more from the safe
| Takefiles(Files : int) |                          

| Userinput() |                                     Enables the safe to take inputted files from the user
| Userinput(Files : Int) |                          


# Step 5


![OOP ACT](<digital safe OOP (2).png>)




# Step 6


Answer these three questions briefly. 
1. Why did you choose this class?   Because i find it simple but taken for granted in our devices

2. Which property do you think is the most important? Why?   The ability to add files in the safe and take them out because this is the core use of the class

3. Which method do you think is the most useful? Why?  The most useful method is Compartments because this allows for organization in the files so you can easily fin where you put a specific file

Your explanation should reflect your own design decisions. This 
