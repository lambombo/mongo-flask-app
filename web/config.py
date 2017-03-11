import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                '51f52814-0071-11e6-a247-000ec6c2372c')

    MONGO_HOST = '192.168.99.100'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'hosts'


class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_HOST = 'localhost'

class ProductionConfig(Config):
    DEBUG = True
    MONGO_HOST = '192.168.99.100'


class TestingConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
