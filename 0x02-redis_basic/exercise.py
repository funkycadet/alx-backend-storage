#!/usr/bin/env python3
""" Exercise module
"""
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class
    A cache class for handling redis data
    """

    def __init__(self):
        """ __init__ method
        This method instantiates private and public
        variables of the class it belongs to
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method
        This method takes data as an argument and
        returns a string while generating a random
        key as well as store the data in Redis and
        and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
