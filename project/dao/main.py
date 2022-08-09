from project.dao.base import BaseDAO
from project.dao.models.directors import Director
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director
