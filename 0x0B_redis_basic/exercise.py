#!/usr/bin/env python3
""" Main file """

import uuid
from typing import Union, Optional, Callable

import redis


class Cache:
    """ Cache class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Retrieve data from redis """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """ Retrieve string data from redis """
        return self.get(key, str)

    def get_int(self, key: str) -> Optional[int]:
        """ Retrieve integer data from redis """
        return self.get(key, int)