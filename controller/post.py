from .base import BaseController
from init.init import PostRepository

class Post(BaseController):
    def __init__(
        self,
        PostRepository
    ):
        self.post = PostRepository
    
    def createPost(self, data):
        result = self.post.createPostRepo(data)
        if result:
            return {'status': 200, 'message': 'Success insterted Post'}
        else:
            return {'status': 400, 'message': 'Failed insterted Post'}
