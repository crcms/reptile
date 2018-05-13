# -*- coding: utf-8 -*-

'''

内容下载

'''

import requests


class Download(object):
    _actuator = None
    _response = None
    _request = {'headers':{}}

    def __init__(self):
        self._actuator = requests

    def handle(self, url, **params):

        if 'headers' in params:
            print(params.get('headers'))
            # self._request_header(params.get('headers'))

        self._response = self._actuator.get(url)

    def _request_header(self, **headers):
        self._request['headers'].update(headers)





if __name__ == '__main__':
    download = Download()
    download.handle('http://thinkphp.cn',headers = dict(x=1,y=2))