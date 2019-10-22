from os import environ
from dotenv import load_dotenv
import redis


class Config:
    load_dotenv()
    # General Config
    #SECRET_KEY = environ.get('SECRET_KEY')
    DEVELOPER = environ.get('DEVELOPER')
    ENVIRONMENT = environ.get('ENVIRONMENT')
    API_KEY = environ.get('API_KEY')
    DEBUG = True

    REDIS_PASS = environ.get('REDIS_PASS')
    REDIS_HOST = environ.get('REDIS_HOST')
    REDIS_PORT = environ.get('REDIS_PORT')
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