from flask import json
from .base import BaseRepository
from module.connection import Connection
from bson.json_util import dumps
import base64
import jwt
from datetime import datetime, timedelta


class AuthRepository(object):
    
    _COLL = 'user'

    def __init__(
        self,
        connection
    ):
        self.connection = connection
        self.jwt = jwt

    def loginRepo(self, data):
        username = data['username']
        password = base64.b64encode(data['password'].encode("utf-8"))

        payload = {
            'username': username,
            'password': password
        }
        data = self.connection._collection(self._COLL).find_one(payload, {'password': False})
        if not data:
            return 'wrong username or password'

        encodeJWT = self.jwt.encode({
            "iss": "restApiFlask",
            "exp": datetime.timestamp(datetime.now() + timedelta(minutes=2)),
            "uid": str(data['_id']),
            'uname': data['username']
        }, 'key', algorithm='HS256')

        result = {
            'token': str(encodeJWT)[2: -1]
        }
        
        return result
    
    def verifyToken(self, authorization):
        try:
            token = authorization[7:]
            prefix = authorization[:7].lower()
            if prefix == "bearer ":
                self.jwt.decode(token, 'key', algorithms='HS256')
                return {'data': True, 'status': 200}
        except jwt.exceptions.ExpiredSignatureError:
            return {'data': False, 'status': 403, 'message': 'Token is Expired'}
        except:
            return {'data': False, 'status': 403, 'message': 'Invalid token'}
            
