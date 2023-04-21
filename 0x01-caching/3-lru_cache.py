#!/usr/bin/python3
'''
LRU Caching
'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A class LRUCache that inherits from BaseCaching
    """
    def __init__(self):
        ''' Initializing class attribute. '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        This function assign the key with a value to the dictionary if
        the key or item is not None, otherwise return nothing, also checks
        if the size of the dictionary higher than MAX_ITEM, if it does it'll
        discard the least recently used item based on LRU algoritm.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        This function returns the value in the dictionary that is linked to
        key, if key is not None and if key exists in dictionary.
        """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
