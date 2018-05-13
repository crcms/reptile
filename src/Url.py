# -*- coding: utf-8 -*-

'''

URL管理

'''


class Url(object):

    _items = []

    def __init__(self):
        pass

    def insert(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop()
