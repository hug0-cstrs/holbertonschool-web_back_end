#!/usr/bin/python3
""" MRU Caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
  """ MRU caching """

  def __init__(self):
    """ Constructor """
    super().__init__()
    self.queue = []  # Initialize an empty list to keep track of the most recently used keys

  def put(self, key, item):
    """ Puts item in cache """
    if key is None or item is None:
      return

    self.cache_data[key] = item  # Add the key-value pair to the cache

    if len(self.cache_data) > BaseCaching.MAX_ITEMS:  # Check if the cache has exceeded its maximum capacity
      if self.queue:  # Check if the queue is not empty
        last = self.queue.pop()  # Remove the last key from the queue
        del self.cache_data[last]  # Remove the corresponding key-value pair from the cache
        print("DISCARD: {}".format(last))  # Print a message indicating the discarded key

    if key not in self.queue:  # Check if the key is not already in the queue
      self.queue.append(key)  # Add the key to the end of the queue
    else:
      self.mv_last_list(key)  # Move the key to the end of the queue

  def get(self, key):
    """ Gets item from cache """
    item = self.cache_data.get(key, None)  # Get the value associated with the key from the cache
    if item is not None:  # Check if the key exists in the cache
      self.mv_last_list(key)  # Move the key to the end of the queue
    return item

  def mv_last_list(self, item):
    """ Moves element to last idx of list """
    length = len(self.queue)
    if self.queue[length - 1] != item:  # Check if the item is not already at the last index of the queue
      self.queue.remove(item)  # Remove the item from its current position in the queue
      self.queue.append(item)  # Add the item to the end of the queue
