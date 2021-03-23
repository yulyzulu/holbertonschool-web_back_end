#!/usr/bin/env python3
""" LFU Caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU class"""

    def __init__(self):
        """Constructor function """
        super().__init__()
        self.older = []

    def put(self, key, item):
        """ Assign values to a dictionary"""
        if (key is not None and item is not None):
            if key in self.cache_data:
                self.older.remove(key)
                del self.cache_data[key]
            self.cache_data[key] = item
            self.older.append(key)
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            old = self.older.pop(0)
            del self.cache_data[old]
            print('DISCARD: ' + old)

    def get(self, key):
        """Return cache data"""
        if (key not in self.cache_data or key is None):
            return None
        else:
            if key in self.cache_data:
                self.older.remove(key)
                self.older.append(key)
            return self.cache_data[key]
