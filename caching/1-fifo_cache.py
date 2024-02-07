#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache"""
    def __init__(self):
        """Constructor"""
        super().__init__() # call init from parent class
        self.queue = [] # create queue

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item: # if key and item are not None
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS: # if cache is at max capacity
                removed = self.queue.pop(0) # remove first item from queue
                del self.cache_data[removed] # remove first item from cache
                print("DISCARD: {}".format(removed)) # print message
            self.queue.append(key) # add key to queue
            self.cache_data[key] = item # add key and item to cache

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None) # return item from cache if key exists, else None
