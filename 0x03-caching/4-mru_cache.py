#!/usr/bin/env python3
""" MRU Caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU class"""

    def __init__(self):
        """Constructor function """
        super().__init__()
        self.keys_cache = []

    def put(self, key, item):
        """ Assign values to a dictionary"""
        if (key is not None and item is not None):
            if key in self.cache_data:
                self.keys_cache.remove(key)
                del self.cache_data[key]
            self.cache_data[key] = item
            self.keys_cache.append(key)
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            last = self.keys_cache[-2:-1]
            del self.cache_data[last[0]]
            print('DISCARD: ' + last[0])

    def get(self, key):
        """Return cache data"""
        if (key not in self.cache_data or key is None):
            return None
        else:
            if key in self.cache_data:
                self.keys_cache.remove(key)
                self.keys_cache.append(key)
            return self.cache_data[key]
