from flask import request
from flask_restx import Namespace, Resource

from project.dao.models.movie import MovieSchema
from project.setup.api.models import movie

from project.setup.api.parsers import page_parser

api = Namespace('movies')

from project.container import movie_service


movie_ns = Namespace('movies')
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@api.route('/')
# @api.doc(params)
class MoviesView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    @movie_ns.doc(description='Get all movies', params={
        'page': 'Page number',
        'status': 'if "new": sort by release year'
    })
    def get(self):
        page = request.args.get('page', type=int)
        status = request.args.get('status')

        movies = movie_service.get_all(page, status)
        return movies_schema.dump(movies), 200
        # """
        # Get all movies.
        # """
        # return movie_service.get_all(**page_parser.parse_args())


@api.route('/<int:movie_id>/')
class MovieView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return movie_service.get_item(movie_id)
