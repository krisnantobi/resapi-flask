from .base import BaseController
from init.init import AuthRepository

class AuthController(BaseController):
    
    def __init__(
        self,
        AuthRepository
    ):
        self.auth = AuthRepository

    def login(self, data):
        result = self.auth.loginRepo(data)
        if result:
            return {
                'data': result,
                'status': 200
            }
        return {
            'data': {},
            'status': 400
        }