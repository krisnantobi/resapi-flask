from flask import request, Response, json, jsonify
from init.init import authController

def initAuth(app):
    
    @app.route('/auth', methods= ['POST'])
    def auth():
        data = request.json
        result = authController.login(data)
        return result, result['status']

    return app