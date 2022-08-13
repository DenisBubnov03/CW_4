import jwt
from flask import request, abort

from project.config import BaseConfig


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, BaseConfig.JWT_SECRET, algorithms=[BaseConfig.JWT_ALGORITHM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs)
    return wrapper