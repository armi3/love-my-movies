import redis
from flask import current_app as app


def create_db():
    redis_client = redis.StrictRedis(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        password=app.config['REDIS_PASS'],
    )
    print(redis_client.get('test'))
    return redis_client
