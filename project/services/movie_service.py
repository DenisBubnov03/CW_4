from typing import Optional
from flask import abort
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.models.movie import Movie
from project.services.base_services import BaseServices


class MoviesService(BaseServices):

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    # def get_all(self, page: Optional[int] = None, sort=None) -> list[Movie]:
    #
    #     return self.dao.get_all(page=page)
    def get_all(self, page=None, status=None):
        """get all movies"""
        movies = self.dao.get_all(page, status=status == 'new')
        if not movies:
            abort(404)

        return movies