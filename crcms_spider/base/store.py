# -*- coding: utf-8 -*-

'''



'''

from abc import ABCMeta, abstractmethod
from mongoengine.document import Document
from datetime import datetime
from crcms_spider.models.data import Data, Const

CONST = Const()


class AbstractStore(metaclass=ABCMeta):

    @abstractmethod
    def create(self, **kwargs): pass


    @abstractmethod
    def update(self, model: Document, **kwargs): pass


    @abstractmethod
    def check_need_update(self, model: Document, timestamp: int) -> bool: pass


    @abstractmethod
    def get_by_url(self, url: str) -> 'AbstractStore' or None: pass


    @abstractmethod
    def get_not_climb(self, limit: int): pass


_current_timestamp = int(datetime.now().timestamp())


class Store(AbstractStore):
    _model = None


    def __init__(self, model: Document):
        self._model = model


    def create(self, **kwargs) -> Document:
        kwargs['status'] = CONST.STATUS_NOT_CRAWLED
        kwargs['created_at'] = _current_timestamp

        return self._model(**kwargs).save()


    def update(self, model: Document, **kwargs) -> Document:
        for key, value in kwargs.items():
            model[key] = value

        model.status = CONST.STATUS_CRAWLED
        model.updated_at = _current_timestamp
        return model.save()


    def check_need_update(self, model: Document, timestamp: int) -> bool:
        return (model.status == CONST.STATUS_CRAWLED and _current_timestamp - model.updated_at > timestamp) or (
                model.status == CONST.STATUS_NOT_CRAWLED)


    def get_by_url(self, url: str) -> 'AbstractStore' or None:
        return self._model.objects(url=url).first()


    def get_not_climb(self, limit: int):
        return self._model.objects(status=CONST.STATUS_NOT_CRAWLED).limit(limit)


if __name__ == '__main__':
    pass
    # import sys
    #
    # print(sys.modules)
    # import random

    # from crcms_spider.models.data import Data

    # print(CONST.STATUS_NOT_CRAWLED)
    # exit()
    # store = Store(Data)
    # url = ''.join(random.sample(
    #     ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
    #      'd', 'c', 'b', 'a'], 5))
    # model = store.create(content='xxxx', url=url)
    # model = store.update(model, content='yyyy')
    # print(model.id)
    # print(store.check_need_update(model, _current_timestamp))
