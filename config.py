from os import environ
import redis


class Config:
    # General Config
    #SECRET_KEY = environ.get('SECRET_KEY')
    DEVELOPER = environ.get('DEVELOPER')
    ENVIRONMENT = environ.get('ENVIRONMENT')
    # FLASK_APP = environ.get('FLASK_APP')
    # FLASK_ENV = environ.get('FLASK_ENV')
    #
    # # Flask-Session
    # SESSION_TYPE = environ.get('SESSION_TYPE')
    # SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))


# class ProdConfig(Config):
#     DEBUG = False
#     TESTING = False
#     # DATABASE_URI = environ.get('DATABASE_URI')
#
#
# class DevConfig(Config):
#     DEBUG = True
#     TESTING = True
#     DATABASE_URI = environ.get('DATABASE_URI')