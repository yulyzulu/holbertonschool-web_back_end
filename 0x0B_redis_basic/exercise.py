#!/usr/bin/env python3
"""
Module to execute functions
"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class"""

    def __init__(self):
        """ Init method that store an instance of the Redis client as
           private variable and flush the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """The method should generate a random key, store the input data
           in Redis using the random key and return the key"""
        id = str(uuid.uuid4())
        self._redis.mset({id: data})
        return id
