# -*- coding: utf-8 -*-

'''



'''
from pymongo import MongoClient

class Connection(object):

    _connect = None

    def __init__(self, address, database = None):
        if database is not None:
            address = address + '/' + database

        self._connect = MongoClient(address)


    @property
    def connect(self):
        return self._connect


    @property
    def close(self):
        self._connect.close()
