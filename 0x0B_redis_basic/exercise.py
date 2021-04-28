#!/usr/bin/env python3
"""
Module to execute functions
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable) -> Union[str, bytes, int, float]:
        """Get method takes a key string argument and optional Callable
           argument """
        data = self._redis.get(key)
        if fn:
            return fn(self._redis.get(data)
        return data

    def get_str(self, data: str) -> str:
        """ Return data to string"""
        self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """ Return data to integer"""
        return int(self._redis.get(data))
