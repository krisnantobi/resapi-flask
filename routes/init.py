from .user import initUser
from .post import initPost

def initRoute(app):
    app = initUser(app)
    app = initPost(app)
    return app