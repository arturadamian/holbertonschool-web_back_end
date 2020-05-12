#!/usr/bin/python3
""" LIFO implementation of coaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.lifo_list = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        print(self.lifo_list)
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
                    print("DISCARD: {}".format(self.lifo_list[3]))
                    del self.cache_data[self.lifo_list[3]]
                    self.lifo_list.pop(3)
                self.cache_data[key] = item
                self.lifo_list.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            val = self.cache_data[key]
            return val
