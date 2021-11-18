# PyMongo

** This source code communicates with MongoDB (a NoSQL database) to Create, Read, Update, and Delete (CRUD) data. **
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
The purpose of this project is to apply database systems concepts and principles in development 
    - This specifically caters to creating a database that can interface with client-side code

The AnimalShelter.py file uses PyMongo to communicate with the database selected to as stated above; create, read, update, and delete.
    - The database created is for a animal shelter wanting to help rescue animals by training them. 
    - A main requirements of this database:
        - Must be able to interact with existing data from the shelter to identify and categorize dogs
        - Will be opensource and accessable on GitHub for accessability and adaptability for other organizations
        - Uses MongoDB for client/server interactive database
    - This project will be full-stack by the completion of the second sprint. This is the progress from sprint 1. 

How it works: 

1) Enabling Mongo on your terminal
    - MongoDB and Python should be installed on your computer. If not, proceed to install. 
    - Locate where they in your file system and follow the commands below to access the mongo shell.
        - You will need to know how to do this later when creating, reading, updating, and deleting items. 
 ![enableMongo](https://user-images.githubusercontent.com/71840637/142474435-bff1d74b-5e6c-4e46-adf1-68d9e8db4105.jpg)
3) The database is imported into MongoDB. This meets the requirement of using existing data in the database. Notice, we moved to the file where mongoDB is located through the terminal. Then used the following command to import the file also located in the same directory. When the data is imported it will display the amount of document imported or if unsuccessful it will state the amount of documents unsuccessfully imported. 

![AACimported](https://user-images.githubusercontent.com/71840637/142472230-756155ab-9493-4d39-a755-145705fa9263.jpg)



**(Ensure MongoDB and Python are installed on the device which you are using the database on. )**
    A demonstration of how it works (its functional operations)
    An identification of the tools used and a rationale for why those tools were chosen
    An explanation of how to reproduce the project

