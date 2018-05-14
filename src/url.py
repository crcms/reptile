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
        return self


    def append(self, item):
        '''

        :param item: item
        :return: self
        '''
        self._items.append(item)
        return self

    # def pop(self):
    #     return self._items.pop()

    def exists(self, item):
        try:
            return self._items.index(item)
        except (ValueError) as e:
            return -1

    def length(self):
        '''

        :return: int
        '''
        return len(self._items)