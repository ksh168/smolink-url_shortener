from flask import Flask

from .extensions import db

def create_app(config_file = 'settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    return app