#!/usr/bin/env python3
"""
Module to execute functions
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that takes a single method Callable arguments
       and return a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        value = method(self, *args)
        self._redis.incr(key)
        return value
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for
        a particular function"""
    input_list = method.__qualname__ + ":inputs"
    output_list = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(input_list, str(*args))
        value = method(self, *args)
        self._redis.rpush(output_list, str(value))
        return value
    return wrapper


class Cache:
    """Cache class"""

    def __init__(self):
        """ Init method that store an instance of the Redis client as
           private variable and flush the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """The method should generate a random key, store the input data
           in Redis using the random key and return the key"""
        id = str(uuid.uuid4())
        self._redis.mset({id: data})
        return id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get method takes a key string argument and optional Callable
           argument """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """ Return data to string"""
        self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """ Return data to integer"""
        return int(self._redis.get(data))
