
from flask import abort
from project.exceptions import ItemNotFound
from project.dao.models.movie import Movie
from project.services.base_services import BaseServices


class MoviesService(BaseServices):

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page=None, status=None):
        """get all movies"""
        movies = self.dao.get_all(page, status=status == 'new')
        if not movies:
            abort(404)

        return movies
