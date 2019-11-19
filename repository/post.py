
from .base import BaseRepository
from module.connection import Connection
import datetime

class PostRepository(BaseRepository):
    
    _COLL = 'post'
    _DEFAULT_DATA = {
        'createdAt': datetime.datetime.utcnow(),
        'updatedAt': datetime.datetime.utcnow()
    }

    def __init__(
        self,
        connection
    ):
        self.connection = connection

    def createPostRepo(self, data):
        insert = self.connection._collection(self._COLL).insert_one(data).inserted_id
        return True