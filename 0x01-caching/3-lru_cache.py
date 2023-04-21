#!/usr/bin/python3
"""
LRU Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """ initializing class attributes """
        super().__init__()
        self.list = []

    def put(self, key, item):
        """
        This function assign the key with a value to the dictionary if
        the key or item is not None, otherwise return nothing, also checks
        if the size of the dictionary higher than MAX_ITEM, if it does it'll
        discard the least recently used item based on LRU algoritm.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.list:
                self.list.append(self.list.pop(self.list.index(key)))
            else:
                self.list.append(key)

            if len(self.list) > BaseCaching.MAX_ITEMS:
                discard_key = self.list.pop(0)
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")

    def get(self, key):
        """
        This function returns the value in the dictionary that is linked to
        key, if key is not None and if key exists in dictionary.
        """
        if key is not None and key in self.cache_data:
            self.list.append(self.list.pop(self.list.index(key)))
            return self.cache_data[key]
        return None
