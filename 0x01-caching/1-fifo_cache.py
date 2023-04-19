#!/usr/bin/env python3
"""
FIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A class FIFOCache that inherits from BaseCaching """
    def put(self, key, item):
        """
        Returns the dictionary's item value for the key, if key or item
        is not None, otherwise checks if the length of the dictionary is
        higher than the MAX_ITEMS, if it does, then DISCARD the first
        element of the dictionary.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: " + next(iter(self.cache_data)))
            del self.cache_data[next(iter(self.cache_data))]

    def get(self, key):
        """
        Returns None, if key is None or if key doesn't exist in the
        dictionary, otherwise the value in the dictionary that is
        linked to the key.
        """
        if key is None and key not in self.cache_data:
            return None
        return self.cache_data[key]
