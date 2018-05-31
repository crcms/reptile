# -*- coding: utf-8 -*-

'''



'''

from datetime import datetime
from mongoengine import *

# from abc import ABCMeta
# from mongoengine.base.metaclasses import TopLevelDocumentMetaclass
# from mongoengine.queryset.queryset import QuerySet

connect('connect', host='mongodb://192.168.150.142:27017/reptile')


# TODO: 元类问题还是需要搞清楚，暂时是可以如此实现
# class DataMeta(ABCMeta, TopLevelDocumentMetaclass):
#     pass
#
#
# STATUS_CRAWLED = 2
# STATUS_NOT_CRAWLED = 1


class Const(object):
    _dict = {
        'STATUS_CRAWLED': 2,
        'STATUS_NOT_CRAWLED': 1
    }


    def __getattr__(self, item: str):
        result = self._dict.get(item.upper())

        if result is None:
            raise AttributeError

        return result


    def __getitem__(self, item: str):

        result = self._dict.get(item.upper())

        if result is None:
            raise AttributeError

        return result


class Data(Document):
    title = StringField(max_length=200)
    url = StringField(max_length=512, unique=True)
    host = StringField(max_length=128)
    created_at = IntField(default=int(datetime.now().timestamp()))
    updated_at = IntField(default=int(datetime.now().timestamp()))
    status = IntField(min_value=1, max_value=2, default=1)  #
    content = StringField()


__all__ = ['Data', 'Const']

if __name__ == '__main__':
    pass
