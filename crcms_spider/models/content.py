# -*- coding: utf-8 -*-

'''



'''

from crcms_spider.models.connnection import Connection
from datetime import datetime


class Content(object):
    _pdo = None

    _database = 'reptile'

    _collection_name = 'contents'

    _collection = None


    def __init__(self):

        self._pdo = Connection('mongodb://192.168.150.142:27017').connect
        self._collection = getattr(getattr(self._pdo, self._database), self._collection_name)


    # def exists(self) -> bool:

    def create(self, kwargs: dict) -> dict:

        if not isinstance(kwargs, dict):
            raise TypeError

        timestamp = int(datetime.now().timestamp())

        try:
            kwargs['created_at'] = timestamp
            kwargs['updated_at'] = timestamp
            # db = self._pdo.reptile
            # collection = self._pdo.contents
            object_id = self._collection.insert_one(kwargs).inserted_id
        except Exception:
            raise Exception
        else:
            kwargs['_id'] = object_id
            return kwargs


    def update(self, id, kwargs: dict):
        if not isinstance(kwargs, dict):
            raise TypeError

        return self._collection.update_one({'_id': id}, {'$set': kwargs})


    def get_not_climb(self, limit: int):
        return [item for item in self._collection.find({'status': 1}).limit(limit)]


    def get_one_by_url(self, url):
        return self._collection.find_one({'url': url})


    def get_one_by_url_status(self, url, status):
        return self._collection.find_one({'url': url, 'status': status})


    def get_one_by_status(self, status):
        return self._collection.find_one({'status': status})


    def __exit__(self, exc_type, exc_val, exc_tb):
        print('--close--')
        self._pdo.close()

if __name__ == '__main__':
    c = Content()
    print(c.create({'x': 1}))
