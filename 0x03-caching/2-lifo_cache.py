#!/usr/bin/env python3
""" Lifo Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO class"""

    def __init__(self):
        """Constructor function """
        super().__init__()
        self.keys_cache = []

    def put(self, key, item):
        """ Assign values to a dictionary"""
        if (key is not None or item is not None):
            self.cache_data[key] = item
            self.keys_cache.append(key)
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            last = self.keys_cache.pop()
            #last = self.cache_data.popitem()
            del self.cache_data[last]
            print('DISCARD: ' + last)

    def get(self, key):
        """Return cache data"""
        if (key not in self.cache_data or key is None):
            return None
        else:
            return self.cache_data[key]
