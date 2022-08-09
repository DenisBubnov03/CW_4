from project.config import config
from project.dao.models.directors import Director
from project.dao.models.genre import Genre
from project.dao.models.movie import Movie
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie" : Movie
    }

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='25000')