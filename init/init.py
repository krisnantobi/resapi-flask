from module.connection import Connection
from repository.user import UserRepository
from controller.user import User

from repository.post import PostRepository
from controller.post import Post

connection = Connection()
userRepo = UserRepository(connection)
userController = User(userRepo)
postRepo = PostRepository(connection)
postController = Post(postRepo)