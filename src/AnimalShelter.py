from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:54086/AAC' % ('aacuser', '1234'))
        self.database = self.client['AAC']
        
# Complete this create method to implement the C in CRUD.

    def create(self, data):
        if data is not None:
            #Insert the data, and return true if successful.
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            #data was invalid.
            raise Exception("Nothing to save, because data parameter is empty")
# Create method to implement the R in CRUD. 
    def read(self, data):
        if data is not None:
            #return all records that match.
            return self.database.animals.find(data)
        else:
            #Data was invalid.
            raise Exception("Nothing to search, because data parameter is empty")
# create method to implement the U in CRUD
    def update(self, data):
        if data is not None:
            self.database.animals.update_one(data)
            return True
        else:
            raise Exception("Cannot locate document to update")
