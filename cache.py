import os
import redis

cache = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'))

def get(key: str):
    return cache.get(key)

def set(key: str, value: str):
    return cache.set(key, value)

def expire(key: str, seconds: int):
    return cache.expire(key, seconds)

