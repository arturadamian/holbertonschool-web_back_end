#!/usr/bin/python3
""" Basic Cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.lru_cache = OrderedDict()
        self.lfu_cache = {}

    def get(self, key):
        """ gets an item from the cache
        """
        if key in self.lru_cache:
            val = self.lru_cache[key]
            self.lru_cache.move_to_end(key)
            if key in self.lfu_cache:
                self.lfu_cache[key] += 1
            else:
                self.lfu_cache[key] = 1
            return val

    def put(self, key, item):
        """ puts an item to the cache"""
        if key in self.lru_cache:
            del self.lru_cache[key]
        self.lru_cache[key] = item
        if key in self.lfu_cache:
            self.lfu_cache[key] += 1
        else:
            self.lfu_cache[key] = 1
        if len(self.lru_cache) > BaseCaching.MAX_ITEMS:
            min_value = min(self.lfu_cache.values())
            lfu_keys = [k for k, v in self.lfu_cache.items() if v == min_value]
            # print(lfu_keys)
            the_key = list(self.lru_cache.items())[0][0]
            if the_key in lfu_keys:
                print("DISCARD:", the_key)
                self.lru_cache.popitem(last=False)
                del self.lfu_cache[the_key]
            else:
                min_key = min(self.lfu_cache, key=self.lfu_cache.get)
                # print(the_actual_key)
                print("DISCARD:", min_key)
                self.lru_cache.popitem(min_key)
                del self.lfu_cache[min_key]
        self.cache_data = dict(self.lru_cache)  # print( self.lfu_cache)
