from .base import BaseController
from init.init import UserRepository

class User(BaseController):
    def __init__(
        self,
        repository: UserRepository
    ):
        self.repository = repository

    def createUser(self, data):
        return self.repository.createUserRepo(data)

    def getUser(self):
        return self.repository.getUserRepo()

    def deleteUser(self, id):
        result = self.repository.deleteUserRepo(id)
        var = "Failed"
        if result:
            var = "Seccess"
            pass
        return var

    def editUser(self, id, data):
        result = self.repository.editUserRepo(id, data)
        var = "Failed"
        if result:
            var = "Seccess"
            pass
        return var

    def detailUser(self, id):
        result = self.repository.detailUserRepo(id)
        return result
