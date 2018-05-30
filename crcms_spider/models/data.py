# -*- coding: utf-8 -*-

'''



'''

from datetime import datetime
# from crcms_spider.base.manager import AbstractUrl
from mongoengine import *

connect('connect', host='mongodb://192.168.150.142:27017/reptile')


class Data(Document):
    title = StringField(max_length=200)
    created_at = IntField(default=int(datetime.now().timestamp()))
    updated_at = IntField(default=int(datetime.now().timestamp()))
    url = StringField()
    status = IntField()#min_value=0, max_value=2, default=1
    content = StringField()



    def check_need_update(self, model: 'AbstractUrl', timestamp: int) -> bool:
        pass


    def get_by_url(self, url: str) -> dict or None:
        pass



if __name__ == '__main__':
    data = Data(title='xxx',content='yyy',url='abc')
    print(data.save())