#!/usr/bin/env python3
"""
Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A class BasicCache that inherits from BaseCaching """
    def put(self, key, item):
        """
        This function returns self.cache_data the item value for the key.

        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        This function returns None if key is None or key doesn't exist in
        self.cache_data, otherwise returns the value in self.cache_data
        linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
