from flask import Response, request, json, jsonify
from init.init import postController

def initPost(app):

    @app.route('/post', methods= ['POST'])
    def createPost():
        data = request.json
        result = postController.createPost(data)
        return jsonify(result), result['status']
    
    return app