#!/usr/bin/env python3
"""
LFU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A class LFUCache that inherits from BaseCaching.
    """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = {}
        self.lfu = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu = min(self.frequency.values())
            if lfu in self.frequency.values():
                for k, v in self.frequency.items():
                    if v == lfu:
                        del self.cache_data[k]
                        del self.frequency[k]
                        break
                print("DISCARD: {}".format(k))

        if key in self.cache_data:
            self.frequency[key] += 1
            self.lfu.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.lfu.pop(0)]
            self.frequency[key] = 1

        self.cache_data[key] = item
        self.lfu.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.lfu.remove(key)
        self.lfu.append(key)

        return self.cache_data[key]
