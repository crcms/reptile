# -*- coding: utf-8 -*-

'''

数据下载

'''

import requests


class Download(object):
    _actuator = None
    _url = None
    _header = None

    def __init__(self, url, Header):
        self._actuator = requests
        self._url = url
        self._header = Header

    def handle(self):
        self._response = self._actuator.get(self._url)
        self._response.encoding = 'utf-8'
        return self

    def responseText(self):
        return self._response.text
