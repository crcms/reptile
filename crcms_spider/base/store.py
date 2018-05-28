# -*- coding: utf-8 -*-

'''



'''

from crcms_spider.models.content import Content
from datetime import datetime

class Store(object):

    def __init__(self):
        pass


    def update(self, id, kwargs):
        kwargs['status'] = 2
        kwargs['updated_at'] = int(datetime.now().timestamp())
        Content().update(id, kwargs)
