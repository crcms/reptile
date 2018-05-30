# -*- coding: utf-8 -*-

'''



'''

from crcms_spider.models.content import Content
from datetime import datetime
from urllib.parse import urlparse
from abc import ABCMeta, abstractmethod


class Url(object):
    _urls = []
    _model = None
    _config = None
    _repeat_update_time = 86400


    def __init__(self, model: Content, config: dict) -> None:
        self._model = model
        self._config = config


    def adds(self, urls: set):
        if not isinstance(urls, set):
            raise TypeError

        new_urls = []
        for url in urls:

            if self._model.get_exists_url(url):
                # 判断是否再次更新
                repeat_update_time = int(self._config.get('repeat_update_time')) or self._repeat_update_time
                result = self._model.get_need_updated_url(url, repeat_update_time)
                if result is not None:
                    if (result['status'] == 2 and int(datetime.now().timestamp()) - result['updated_at']) < int(
                            self._config.get('repeat_update_time')) or self._repeat_update_time:
                        continue
            else:

                result = self._model.create({
                    'host': urlparse(url).netloc,
                    'url': url,
                    'status': 1
                })

            # TODO 写入数据库
            new_urls.append(result)

        # 保存至内存操作
        self._store_memory(new_urls)


    def _store_memory(self, urls):

        if len(self._urls) < 500:
            self._urls = self._urls[len(self._urls) - 1:] = urls


    def get_url(self) -> dict or None:
        if len(self._urls) == 0:
            self._urls = Content().get_not_climb(500)

        if len(self._urls) == 0:
            return None
        # print(self._urls)
        return self._urls.pop()


class AbstractUrl(metaclass=ABCMeta):

    @abstractmethod
    def check_need_update(self, model: 'AbstractUrl', timestamp: int) -> bool: pass


    @abstractmethod
    def get_by_url(self, url: str) -> dict or None: pass


if __name__ == '__main__':
    from pymongo import MongoClient

    # Content().get_by_url('')

    result = Content().create({
        'url': 'abc',
        'status': 1
    })
    print(Content().update(result['_id'], {'$set': {'url': 123, 'xx': 'ss'}}))
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
