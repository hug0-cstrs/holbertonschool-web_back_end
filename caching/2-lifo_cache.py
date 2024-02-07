#!/usr/bin/python3

""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
  """ LIFO caching """

  def __init__(self):
    """ Constructor """
    super().__init__()
    self.queue = []  # Initialize an empty list to store the keys in the order they were added

  def put(self, key, item):
    """ Puts item in cache """
    if key is None or item is None:
      return

    self.cache_data[key] = item  # Add the key-value pair to the cache

    if len(self.cache_data) > BaseCaching.MAX_ITEMS:  # Check if the cache has exceeded the maximum number of items
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
    return self.cache_data.get(key, None)  # Return the value associated with the key from the cache, or None if the key is not found

  def mv_last_list(self, item):
    """ Moves element to last idx of list """
    length = len(self.queue)
    if self.queue[length - 1] != item:  # Check if the last key in the queue is not the same as the given key
      self.queue.remove(item)  # Remove the given key from the queue
      self.queue.append(item)  # Add the given key to the end of the queue
