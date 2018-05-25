# -*- coding: utf-8 -*-

'''

数据下载响应

'''

import requests
from modules.download.request import Request


class Response(object):
    _actuator = None
    _request = None

    _encoding = 'utf-8'


    def __init__(self, request: Request) -> 'Response':
        """

        :param Request:
        """
        self._actuator = requests
        self._request = request

        self._handle().set_encoding(self._encoding)


    def _handle(self) -> 'Response':
        payload = {}

        if self._request.method == 'get':
            payload['params'] = self._request.payload
        elif self._request.method == 'post':
            payload['data'] = self._request.payload

        try:
            self._response = getattr(self._actuator, self._request.method)(self._request.url, headers=self._request.headers,
                                                                       **payload)
        except requests.exceptions.RequestException as e:
            print(e.strerror)

        return self


    @property
    def response(self) -> 'requests.models.Response':
        return self._response


    @property
    def responseText(self) -> str:
        return self._response.text


    @property
    def request(self) -> Request:
        return self._request


    def set_encoding(self, encoding) -> 'Response':
        self._encoding = encoding
        self._response.encoding = self._encoding
        return self


if __name__ == '__main__':
    # from modules.download.request import Request

    response = Response(Request('http://thinkphp.cn')).set_encoding('utf-8')
    # Response(request)
    print(response.responseText)
