# -*- coding: utf-8 -*-

'''



'''

from urllib.parse import urlparse
from abc import ABCMeta, abstractmethod


class AbstractUrl(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def check_need_update(model: 'AbstractUrl', timestamp: int) -> bool: pass

    @staticmethod
    @abstractmethod
    def get_by_url(url: str) -> 'AbstractUrl' or None: pass

    @staticmethod
    @abstractmethod
    def get_not_climb(limit: int): pass

    @staticmethod
    @abstractmethod
    def create(**kwargs) -> 'AbstractUrl': pass

    @staticmethod
    @abstractmethod
    def update(model: 'AbstractUrl', **kwargs):pass


class Url(object):
    _urls = []
    _model = None
    _config = None
    _repeat_update_time = 86400

    def __init__(self, model: AbstractUrl, config: dict) -> None:
        self._model = model
        self._config = config

    def adds(self, urls: set):
        if not isinstance(urls, set):
            raise TypeError

        new_urls = []
        for url in urls:

            result = self._model.get_by_url(url)

            if result is not None:
                # 判断是否再次更新
                repeat_update_time = int(self._config.get('repeat_update_time')) or self._repeat_update_time
                if not self._model.check_need_update(result, repeat_update_time):
                    continue
            else:
                result = self._model.create(
                    host=urlparse(url).netloc,
                    url=url,
                )

            # 写入数据库
            new_urls.append(result)

        # 保存至内存操作
        self._store_memory(new_urls)

    def _store_memory(self, urls):

        if len(self._urls) < 500:
            self._urls = self._urls[len(self._urls) - 1:] = urls

    def get_url(self) -> dict or None:
        if len(self._urls) == 0:
            self._urls = list(self._model.get_not_climb(500))

        if len(self._urls) == 0:
            return None
        # print(self._urls)
        return self._urls.pop()


if __name__ == '__main__':
    from pymongo import MongoClient

    # Content().get_by_url('')

    # result = Content().create({
    #     'url': 'abc',
    #     'status': 1
    # })
    # print(Content().update(result['_id'], {'$set': {'url': 123, 'xx': 'ss'}}))
    # print(Content().get_one_by_url_status('abc', 1))

    # print(Content().get_not_climb(500))
    # for object in Content().get_not_climb(500):
    #     print(object)
    # print(Content().get_not_climb(500))

    # print(result)

    # client = MongoClient('192.168.150.142',27017)
    # db = client.reptile
    # collection = db.tests
    # id = collection.insert_one({'url':'https://baidu.com','content':'xxxx','updated_at':int(datetime.now().timestamp())}).inserted_id
    # print(type(id))
    # x = collection.find_one({"_id": str(id)+'x'})
    # print(x)
    # print(123)
