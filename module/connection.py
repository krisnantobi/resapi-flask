
from pymongo import MongoClient

class Connection(object):
    
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.testDB2

    '''
        get collection from db according to param collection
    '''
    def _collection(self, collection):
        col = self.db[collection]
        return col