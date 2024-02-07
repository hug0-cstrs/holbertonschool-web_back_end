#!/usr/bin/python3
""" Basic Dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """Puts item in cache"""
        if key is not None and item is not None: # if key and item are not None
            self.cache_data[key] = item # add key and item to cache

    def get(self, key):
        """Gets item from cache"""
        return self.cache_data.get(key, None) # return item from cache if key exists, else None
