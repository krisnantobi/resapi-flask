from .user import initUser
from .post import initPost
from .auth import initAuth

def initRoute(app):
    app = initUser(app)
    app = initPost(app)
    app = initAuth(app)
    return app