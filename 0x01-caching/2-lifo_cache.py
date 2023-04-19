#!/usr/bin/env python3
"""
LIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A class LIFOCache that inherits from BaseCaching """
    def __init__(self):
        """ initializing class """
        super().__init__()
        self.a = []

    def put(self, key, item):
        """
        Returns self.cache_data the items value for the key, if key is
        not None or item is not None, also discard the last item in cache
        based on LIFO algorithm
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.a:
                self.a.append(key)
            self.a.append(self.a.pop(self.a.index(key)))
        if len(self.a) > BaseCaching.MAX_ITEMS:
            last = self.a.pop(-2)
            del self.cache_data[last]
            print("DISCARD: " + last)

    def get(self, key):
        """
        Returns self.cache_data linked to key, if key is not None or key
        exists in self.cache_data, otherwise None.
        """
        if key is None and key not in self.cache_data:
            return None
        return self.cache_data[key]
