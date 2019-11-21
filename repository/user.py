from .base import BaseRepository
from module.connection import Connection
from bson.json_util import dumps
from flask import json
from bson import ObjectId

from cryptography.fernet import Fernet
from config.config import PASSWORD_KEY

import datetime
import base64

class UserRepository(BaseRepository):
    def __init__(
        self,
        connection: Connection
    ):
        self.connection = connection
        self.fernet = Fernet(PASSWORD_KEY)

    DEFAULT_DATA = {
        'date' : datetime.datetime.utcnow()
    }
    _COLLECTION = 'user'

    def createUserRepo(self, data):
        data['password'] = base64.b64encode(data['password'].encode("utf-8"))
        finalData = {**data, **self.DEFAULT_DATA}
        insert = self.connection._collection(self._COLLECTION).insert_one(finalData).inserted_id
        return str(insert)

    def getUserRepo(self):
        result = self.connection._collection(self._COLLECTION).find({}, {'name' : True})
        return json.loads(dumps(result))
        
    def deleteUserRepo(self, id):
        id = ObjectId(id)
        result = self.connection._collection(self._COLLECTION).delete_one({'_id' : id })
        return True

    def detailUserRepo(self, id):
        id = ObjectId(id)
        result = self.connection._collection(self._COLLECTION).find_one({'_id': id})
        result['_id'] = str(result['_id'])
        return json.loads(dumps(result))

    def editUserRepo(self, id, data):
        id = ObjectId(id)
        data = {
            'name': data['name'] 
        }
        result = self.connection._collection(self._COLLECTION).update_one({'_id' : id }, {'$set': data})
        return True