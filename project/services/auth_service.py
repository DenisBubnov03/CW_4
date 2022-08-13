import calendar
import datetime

from flask import current_app

from ..config import BaseConfig
import jwt
from flask_restx import abort


from project.services.user_services import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise abort(400)
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                print(user.username, user.password)
                abort(400)

        data = {
            'email': user.email
        }

        # 30 min for access_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, BaseConfig.JWT_SECRET, algorithm=BaseConfig.JWT_ALGORITHM)

        # 130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, BaseConfig.JWT_SECRET, algorithm=BaseConfig.JWT_ALGORITHM)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def get_email(self, refresh_token):
        """get email by refresh token"""
        data = jwt.decode(refresh_token,
                          current_app.config.get('JWT_SECRET'),
                          algorithms=[current_app.config.get('JWT_ALGORITHM')])
        return data.get('email')

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=BaseConfig.JWT_SECRET, algorithms=[BaseConfig.JWT_ALGORITHM])
        username = data.get("username")

        return self.generate_tokens(username, None, is_refresh=True)
