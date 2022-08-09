import os, sys

from project.setup.db import db

path = os.path.abspath('.')
sys.path.insert(1, path)

from project.config import DevelopmentConfig
from project.dao.models import genre, directors, movie, user
from project.server import create_app

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
