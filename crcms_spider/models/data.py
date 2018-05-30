# -*- coding: utf-8 -*-

'''



'''

from datetime import datetime
from crcms_spider.base.manager import AbstractUrl
from mongoengine import connect


connect(host = 'mongodb://192.168.150.142:27017')

# class Data(AbstractUrl,Document):