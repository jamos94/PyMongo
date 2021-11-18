# PyMongo

Using MongoDB (a NoSQL database) and Python to Create, Read, Update, and Delete (CRUD) data. 
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
 
3) Importing a database (csv file) in the terminal (Mongo import tool) 
- The database is imported into MongoDB.  
- Notice, we moved to the file where MongoDB is located through the terminal. 
- Then used the following command to import the file also located in the same directory. 
    - When the data is imported it will display the amount of document imported or if unsuccessful it will state the amount of documents unsuccessfully imported.
        -   NOTICE: This is done through the terminal, not the Mongo shell
        -   This meets the requirement of using existing data in the database.
![AACimported](https://user-images.githubusercontent.com/71840637/142472230-756155ab-9493-4d39-a755-145705fa9263.jpg)

4) Create User Accounts
- User accounts increase security through user authentication to databases and collections
- We will create an admin account and a user account for the AAC database we imported
    - The admin account will have access to all databases, while the AAC user account only has access to the AAC database.
    ![createAdmin](https://user-images.githubusercontent.com/71840637/142476997-47b91b2d-dad2-4901-8dfc-cd83b059d26a.jpg)
    ![createUserAAC](https://user-images.githubusercontent.com/71840637/142477051-89857b85-c8c8-4f90-a68a-144c225f75e3.jpg)
    
- These screenshots display the mongo commands required to create a new user account. We can adjust specifications to meet the user's privelages. 

5) Develop a CRUD class (create, read, update, delete)
- Using Python, develop a 'create' object to insert a document into MongoDB database and collection
    - This program will input an argument to a function that will set a value in the data type acceptable to the MongoDB driver (insert API call)
         - If successful the result will be returned
         - If unsuccessful, the result will return False
- Using Python, develop a 'read' object that querries a document(s) from the database or collection 
    - Uses key/value lookup pair to use with MongoDB driver (find API call) 
        - if successful return results
        - if unsuccessful, return an error message 
![AnimalShelter](https://user-images.githubusercontent.com/71840637/142479240-216a9329-a5b9-4351-9f76-734193719eb9.jpg)

- _more functionality will be added to AnimalShelter.py file in the coming sprint to incorporate all aspects of CRUD into the database

--
More on the Tools Used: 
- MongoDB  -- Instalation: https://docs.mongodb.com/guides/server/install/
    - A document database for application development and cloud. MongoDB is powerful because it uses nodes when adding data to share the load.
    - Access documents and collections with high-availability and the ability to scale as your data grows.
    - Mongo has a large collection of documentation on how to use their tools. Check out the mongo Documentation section of their website for detailed information about all things mongo related. 
    - If you'd like to learn more about MongoDB here's a link to their main webiste which breaks it down completely.
        - https://www.mongodb.com/basics 
- mongo shell 
    - This is where the magic is happening. 
    - All commmands are entered here and CRUD can be used
    - Here is more information about the shell 
        - https://docs.mongodb.com/manual/reference/program/mongo/#mongodb-binary-bin.mongo
- mongoimport 
    -  We used this command in the terminal to import our database. 
    -  I have been using linux so these commands are relevant to my OS. However, here is a link to where you can an OS: https://docs.mongodb.com/guides/server/import/
    -  Where <> replacce with your authentication. If you have not created authentication yet, omit the second lines. 

      mongoimport --db test --collection inventory 
          --authenticationDatabase admin -u <user> -p <password>
          --drop --file ~\downloads\inventory.crud.json
- Create User
    - Creating a user secures your databases through authentication!
    - In the mongo shell, complete the commands as listed in step 4 of How It Works or refer to the link for more specific instructions
        -  https://docs.mongodb.com/guides/server/auth/index.html
- Understanding CRUD
    - There are more operating that can be implemented using CRUD than are listed in this documentatio so far. 
    - As stated above we know CRUD stands for create, read, update, and delete. This increases the functionality of our database.
    - For more information on CRUD operations: https://docs.mongodb.com/manual/crud/

