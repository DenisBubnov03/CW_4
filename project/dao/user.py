from project.dao.base import BaseDAO
from project.dao.models.user import User


class UserDAO(BaseDAO):

    def get_by_email(self, email):
        try:
            email = self._db_session.query(User).filter(User.email == email).one()
            return email
        except:
            return None

    def create(self, user_data):
        entity = User(**user_data)
        self._db_session.add(entity)
        self._db_session.commit()
        return entity

    def update_email(self, data, email):
        self._db_session.query(User).filter(User.email == email).update(data)
        self._db_session.commit()
