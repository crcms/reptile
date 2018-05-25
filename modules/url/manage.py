# -*- coding: utf-8 -*-

'''



'''

from models.content import Content
from datetime import datetime
from urllib.parse import urlparse

class Url(object):
    _urls = []


    def __init__(self):
        pass


    def adds(self, urls: set):
        if not isinstance(urls, set):
            raise TypeError

        content = Content()
        new_urls = []
        for url in urls:
            # TODO 判断是否再次更新
            result = content.get_one_by_url(url)
            if result is not None:
                if (result['status'] == 2 and int(datetime.now().timestamp()) - result['updated_at']) < 86400:
                    continue
            else:
                # TODO 写入数据库
                result = content.create({
                    'host': urlparse(url).netloc,
                    'url': url,
                    'status': 1
                })

            new_urls.append(result)

        # 保存至内存操作
        self._store_memory(new_urls)


    def _store_memory(self, urls):

        if len(self._urls) < 500:
            self._urls = self._urls[len(self._urls)-1:] = urls


    def get_url(self) -> dict or None:
        if len(self._urls) == 0:
            self._urls = Content().get_not_climb(500)

        if len(self._urls) == 0:
            return None
        # print(self._urls)
        return self._urls.pop()


if __name__ == '__main__':
    from pymongo import MongoClient

    # Content().get_by_url('')

    result = Content().create({
        'url': 'abc',
        'status': 1
    })
    print(Content().update(result['_id'],{'$set':{'url':123,'xx':'ss'}}))
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
