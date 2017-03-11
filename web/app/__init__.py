import os

from flask import Flask
from config import config
from flask_pymongo import PyMongo, pymongo
#from ext import mongo
mongo = PyMongo()

def create_app(config_name=None, main=True):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize flask extensions
    mongo.init_app(app)

    # Register API routes
    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .analytics import analytics as analytics_blueprint
    app.register_blueprint(analytics_blueprint, url_prefix = '/analytics')

    return app
