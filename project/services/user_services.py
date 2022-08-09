import base64
import hashlib
import hmac

from project.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from project.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, name):
        return self.dao.get_by_username(name)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data["password"] = self.get_password_hash(user_data.get("password"))
        return self.dao.create(user_data)

    def delete(self, uid):
        return self.dao.delete(uid)

    def update(self, user_data):
        user_data["password"] = self.get_password_hash(user_data.get("password"))
        return self.dao.update(user_data)

    def get_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac('sha256',
                                          other_password.encode('utf-8'),
                                          PWD_HASH_SALT,
                                          PWD_HASH_ITERATIONS)
        print(decoded_digest, hash_digest)
        return hmac.compare_digest(decoded_digest, hash_digest)
