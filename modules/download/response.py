# -*- coding: utf-8 -*-

'''

数据下载

'''

import requests

from modules.download.request import Request

class Response(object):
    _actuator = None
    _request = None

    _encoding = 'utf-8'

    def __init__(self, request):
        """

        :param Request:
        """
        self._actuator = requests
        self._request = Request

        self._handle().set_encoding(self._encoding)

    def _handle(self):
        payload = {}

        if self._request.method == 'get':
            payload['params'] = self._request.payload
        elif self._request.method == 'post':
            payload['data'] = self._request.payload

        self._response = getattr(self._actuator, self._request.method)(self._request.url, headers=self._request.headers,
                                                                       **payload)
        return self

    @property
    def response(self):
        return self._response

    @property
    def responseText(self):
        return self._response.text

    @property
    def request(self):
        return self._request

    def set_encoding(self, encoding):
        self._encoding = encoding
        self._response.encoding = self._encoding
        return self


if __name__ == '__main__':
    # from modules.download.request import Request

    response = Response(Request('http://thinkphp.cn')).set_encoding('utf-8')
    # Response(request)
    print(response.responseText)
