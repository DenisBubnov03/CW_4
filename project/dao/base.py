from typing import Generic, Optional, TypeVar

from flask import current_app
from sqlalchemy import desc
from sqlalchemy.orm import scoped_session
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session, status, model) -> None:
        self._db_session = db_session
        self.status = status
        self.model = model

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, pk: int) -> Optional[T]:
        return self._db_session.query(self.__model__).get(pk)

    def get_all(self, page=None, status=False):
        """get all items"""
        content = self._db_session.query(self.model)

        if status:
            content = content.order_by(desc(self.model.year))
        if page:
            content = content.limit(current_app.config.get('ITEMS_PER_PAGE')).offset(
                (page - 1) * current_app.config.get('ITEMS_PER_PAGE'))

        return content.all()

