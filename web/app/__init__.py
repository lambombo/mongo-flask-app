import os

from flask import Flask
from config import config
from flask_pymongo import PyMongo, pymongo


# Flask extensions
mongo = PyMongo()


def create_app(config_name=None, main=True):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])


    # Initialize flask extensions
    mongo.init_app(app)

    # Register web application routes
    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register API routes
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
