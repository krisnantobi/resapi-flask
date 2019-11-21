
from functools import wraps
from init.init import authRepo
from flask import request

def checkAuth(fn):
    
    @wraps(fn)
    def wrapper(*args, **kwargs):
        headers = request.headers
        auth = authRepo.verifyToken(headers.get('Authorization'))
        if not auth['data']:
            return auth, auth['status']
        return fn(*args, **kwargs)
    return wrapper