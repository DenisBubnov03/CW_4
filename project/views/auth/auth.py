from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service

api = Namespace("auth")


@api.route("/register/")
class AuthsRegView(Resource):

    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        if None in [email, password]:
            abort(400)

        data = {
            "email": email,
            "password": password
        }
        user = user_service.create(data)
        return "", 201, {"location": f"/user/{user.id}"}


@api.route('/login/')
class AuthsLogView(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        if None in [email, password]:
            abort(400)

        return auth_service.generate_tokens(email, password), 201

    def put(self):
        refresh_token = request.json.get("refresh_token")

        if not refresh_token:
            abort(400)

        return  auth_service.approve_refresh_token(refresh_token), 201
