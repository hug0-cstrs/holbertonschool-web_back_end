#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
  """ LRU caching """

  def __init__(self):
    """ Constructor """
    super().__init__()
    self.queue = []  # Queue to keep track of the least recently used items

  def put(self, key, item):
    """ Puts item in cache """
    if key is None or item is None:
      return

    self.cache_data[key] = item  # Add item to the cache

    if len(self.cache_data) > BaseCaching.MAX_ITEMS:
      removed = self.queue.pop(0)  # Remove the least recently used item from the queue
      del self.cache_data[removed]  # Remove the least recently used item from the cache
      print("DISCARD: {}".format(removed))  # Print the discarded item

    if key in self.queue:
      self.queue.remove(key)  # Remove the key from the queue if it already exists
    self.queue.append(key)  # Add the key to the end of the queue

  def get(self, key):
    """ Gets item from cache """
    if key in self.queue:
      self.queue.remove(key)  # Remove the key from the queue
      self.queue.append(key)  # Add the key to the end of the queue
    return self.cache_data.get(key, None)  # Return the item from the cache, or None if not found
