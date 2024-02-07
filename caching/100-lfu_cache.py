#!/usr/bin/python3

""" LFU Caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
  """ LFU caching """

  def __init__(self):
    """ Constructor """
    super().__init__()
    self.queue = []  # Queue to keep track of the order of items
    self.counter = {}  # Dictionary to keep track of the frequency of items

  def put(self, key, item):
    """ Puts item in cache """
    if key is None or item is None:
      return

    self.cache_data[key] = item  # Add item to the cache

    item_count = self.counter.get(key, None)  # Get the frequency of the item

    if item_count is not None:
      self.counter[key] += 1  # Increment the frequency if the item already exists
    else:
      self.counter[key] = 1  # Set the frequency to 1 if the item is new

    if len(self.cache_data) > BaseCaching.MAX_ITEMS:
      first = self.get_first_list(self.queue)  # Get the least frequently used item
      if first:
        self.queue.pop(0)  # Remove the least frequently used item from the queue
        del self.cache_data[first]  # Remove the least frequently used item from the cache
        del self.counter[first]  # Remove the frequency of the least frequently used item
        print("DISCARD: {}".format(first))  # Print a message indicating the discarded item

    if key not in self.queue:
      self.queue.insert(0, key)  # Add the item to the front of the queue
    self.mv_right_list(key)  # Move the item to the right in the queue

  def get(self, key):
    """ Gets item from cache """
    item = self.cache_data.get(key, None)  # Get the item from the cache
    if item is not None:
      self.counter[key] += 1  # Increment the frequency of the item
      self.mv_right_list(key)  # Move the item to the right in the queue
    return item

  def mv_right_list(self, item):
    """ Moves element to the right, taking into account LFU """
    length = len(self.queue)

    idx = self.queue.index(item)  # Get the index of the item in the queue
    item_count = self.counter[item]  # Get the frequency of the item

    for i in range(idx, length):
      if i != (length - 1):
        nxt = self.queue[i + 1]  # Get the next item in the queue
        nxt_count = self.counter[nxt]  # Get the frequency of the next item

        if nxt_count > item_count:
          break

    self.queue.insert(i + 1, item)  # Insert the item to the right in the queue
    self.queue.remove(item)  # Remove the item from its previous position in the queue

  @staticmethod
  def get_first_list(array):
    """ Get first element of list or None """
    return array[0] if array else None  # Return the first element of the list or None if the list is empty
