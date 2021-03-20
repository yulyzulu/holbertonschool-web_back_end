#!/usr/bin/env python3
""" Basic dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic class"""

    def __init__(self):
        """Constructor function """
        super().__init__()

    def put(self, key, item):
        """ Assign values to a dictionary"""
        if (key is not None or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """Return cache data"""
        if (key not in self.cache_data or key is None):
            return None
        else:
            return self.cache_data[key]
