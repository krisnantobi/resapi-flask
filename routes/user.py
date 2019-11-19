from flask import request, Response, json, jsonify
from init.init import userController


def initUser(app):

    @app.route('/users', methods= ["POST"])
    def createUser():
        data = request.json
        
        result = userController.createUser(data)
        return jsonify({
            'data': result,
            'message': 'success'
        }), 200

    @app.route('/users', methods= ["GET"])
    def getUser():
        result = userController.getUser()
        return jsonify({
            'data': result,
            'message': 'success'
        })

    @app.route('/users/<var>', methods= ['DELETE'])
    def deleteUser(var):
        result = userController.deleteUser(var)
        return jsonify({
            'data': [],
            'message': result
        })

    @app.route('/users/<var>/edit', methods= ['PUT'])
    def editUser(var):
        data = request.json
        result = userController.editUser(var, data)
        return jsonify({
            'data': [],
            'message': result
        })

    return app