# PyMongo

Using MongoDB and Python to Create, Read, Update, and Delete (CRUD) data. 
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
![enableMongo](https://user-images.githubusercontent.com/71840637/143285034-04cfb086-8e96-4217-a9b2-f23e98173a17.jpg)

 
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
    - The admin account will have access to all databases, while the AAC user account only has access to the AAC database
    - the user should database should be associated with the database they will need access to
    - I had to go back and adjust this users db and roles for AAC and readWrite as shown it possess in the 2nd image
    - after you create an account, run the commands in the second screenshot to preview your new user and double check roles
    ![createUserAAC](https://user-images.githubusercontent.com/71840637/143290020-709bd547-d95c-4992-80d8-6d96d0c84cf3.jpg)
    ![aacuserInAACdb](https://user-images.githubusercontent.com/71840637/143289623-4194adb5-8ce3-4a29-a9a9-a5db476f3149.jpg)

    
- These screenshots display the mongo commands required to create a new user account. We can adjust specifications to meet the user's privelages. 

5) Develop a CRUD class (create, read, update, delete)
- Using Python, develop a 'create' object to insert a document into MongoDB database and collection
- ensure that you adjust the port number to the port listed when you began mongoDB in step one
    - This program will input an argument to a function that will set a value in the data type acceptable to the MongoDB driver (insert API call)
         - If successful the result will be returned
         - If unsuccessful, the result will return False
- Using Python, develop a 'read' object that querries a document(s) from the database or collection 
    - Uses key/value lookup pair to use with MongoDB driver (find API call) 
        - if successful return results
        - if unsuccessful, return an error message 
![CRUD](https://user-images.githubusercontent.com/71840637/146575914-286e7680-d2d5-4911-99c4-e759f3f8020f.jpg)

6) Develop a testing script
- a test script will ensure functionality of the database's new functions, read and insert. 
- This is a .ipynb file.
- If it is funtional the output will be True
![scriptTestSUCCESS](https://user-images.githubusercontent.com/71840637/146576080-c2e1f09e-f350-4a45-9f7e-a336a6b0e6cc.jpg)

7) Create a user interface
- Create another ipynb notebook and develop code using plotly and dash to integrate front-end user functionality. 
- User interfaces can be constructed using tables, graphs and maps to display data. Sorting and filters are added for user interaction with the data. 
 ![image](https://user-images.githubusercontent.com/71840637/146576231-56fedfda-2afa-4481-8800-fb497bf08afe.png)

-more specific types of filtering can be used through building queries, adding buttons, slides, or drop downs. You can also set the table to be editable if needed. In this case the data is only being displayed so it is not. See plotly dash for specifics

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
- Jupyter
    -  when using juypter to access and test the database, ensure that mongo is running in the database that you would like to use.
        - mongo -u "aacuser" --authenticationDatabase "AAC" -p
            - this will prompt for password
    - once mongo is accessed through the appropriate user switch to that data base using the 'use dbs' command
            - use AAC
    - now you should be able open jupyter and run the files successfully
        ![scriptTestSUCCESS](https://user-images.githubusercontent.com/71840637/143291079-ef8abebf-580d-4c54-b9e1-e478dfcfd807.jpg)
