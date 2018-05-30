# -*- coding: utf-8 -*-

'''



'''

from datetime import datetime
from crcms_spider.base.manager import AbstractUrl
from mongoengine import *
from abc import ABCMeta
from mongoengine.base.metaclasses import TopLevelDocumentMetaclass
from mongoengine.queryset.queryset import QuerySet

connect('connect', host='mongodb://192.168.1.106:27017/reptile')


# TODO: 元类问题还是需要搞清楚，暂时是可以如此实现
class DataMeta(ABCMeta, TopLevelDocumentMetaclass):
    pass


STATUS_CRAWLED = 2
STATUS_NOT_CRAWLED = 1

class Data(AbstractUrl, Document, metaclass=DataMeta):

    title = StringField(max_length=200)
    url = StringField(max_length=512, unique=True)
    host = StringField(max_length=128)
    created_at = IntField(default=int(datetime.now().timestamp()))
    updated_at = IntField(default=int(datetime.now().timestamp()))
    status = IntField(min_value=1, max_value=2, default=STATUS_NOT_CRAWLED)  #
    content = StringField()

    @staticmethod
    def check_need_update(model: 'AbstractUrl', timestamp: int) -> bool:
        current_timestamp = int(datetime.now().timestamp())
        return (model.status == STATUS_CRAWLED and current_timestamp - model.updated_at > timestamp) or (
                model.status == STATUS_NOT_CRAWLED)

    @staticmethod
    def get_by_url(url: str) -> 'AbstractUrl' or None:
        return Data.objects(url=url).first()

    @staticmethod
    def get_not_climb(limit: int):
        return Data.objects(status=STATUS_NOT_CRAWLED).limit(limit)

    @staticmethod
    def create(**kwargs) -> 'AbstractUrl':
        kwargs['status'] = STATUS_NOT_CRAWLED
        return Data(**kwargs).save()

    @staticmethod
    def update(model: 'AbstractUrl', **kwargs):
        for key, value in kwargs.items():
            model[key] = value

        model.status = STATUS_CRAWLED
        model.save()
        return model


if __name__ == '__main__':
    # data = Data(title='xxx', content='yyy', url='fdafdasfasfsa')
    # x = data.save()
    # print(type(x))
    # x = Data.objects(url='fdafdasfasfsa').first()
    # print(type(x))
    print(type(Data.get_not_climb(20)))
