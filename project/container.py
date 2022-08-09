from project.dao import GenresDAO
from project.dao.main import DirectorDAO
from project.dao.main import MovieDAO
from project.dao.models.directors import Director
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie

from project.services import GenresService, DirectorsService, MoviesService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session, status=None, model=Genre)

# Services
genre_service = GenresService(dao=genre_dao)

# DAO
movie_dao = MovieDAO(db.session, status=None, model=Movie)
# Services
movie_service = MoviesService(dao=movie_dao)

# DAO
director_dao = DirectorDAO(db.session, status=None, model=Director)

# Service
director_service = DirectorsService(dao=director_dao)
