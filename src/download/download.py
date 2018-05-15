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
            self._request_header(params.get('headers'))

        self._response = self._actuator.get(url)
        self._response.encoding = 'utf-8'
        return self._response.text


    def _request_header(self, headers):
        '''
        默认header设置
        :param headers: dict
        :return: self
        '''
        defaultHeaders = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        defaultHeaders = defaultHeaders.update(headers)
        self._request['headers'] = defaultHeaders

        return self




if __name__ == '__main__':
    download = Download()
    headersParams = {
        'host':'www.thinkphp.cn',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    download.handle('http://www.thinkphp.cn/document/index.html',headers = headersParams)