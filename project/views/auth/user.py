from flask import request
from flask_restx import Resource, Namespace

from project.container import user_service, auth_service
from project.dao.models.user import UserSchema
from project.decorators import auth_required

api = Namespace('user')
user_schema = UserSchema()




@api.route('/')
class UserView(Resource):
    @auth_required
    @api.doc(description='Get user by token')
    def get(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = auth_service.get_email(token)

        user = user_service.get_by_email(email)
        return user_schema.dump(user), 200

    @auth_required
    @api.doc(description='Update user info(name, surname, fav genre)')
    def patch(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = auth_service.get_email(token)

        updated_data = user_schema.dump(request.json)
        user_service.update_info(updated_data, email)
        return "", 200


@api.route('/password/')
class PasswordView(Resource):
    @auth_required
    @api.doc(description='Update user password')
    def put(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = auth_service.get_email(token)

        passwords = request.json
        user_service.update_password(passwords, email)
        return "", 200