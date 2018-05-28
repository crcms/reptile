# -*- coding: utf-8 -*-

'''



'''
import requests


class Request(object):
    _headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'connection': 'keep-alive',
    }

    _cookies = {}

    _payload = {}

    _method = 'get'

    _allowMethods = set(['get', 'post', 'delete', 'options', 'head', 'put', 'update'])

    _url = None


    def __init__(self, url: str, method: str = 'get', headers: dict = {}, payload: dict = {}, cookies: dict = {},
                 **kwargs) -> None:
        '''
        header设置
        :param kwargs: dict header选项
        '''

        self.set_url(url).set_method(method)

        if len(headers) > 0:
            self._headers.update(headers)

        if len(payload) > 0:
            self._payload.update(payload)

        if len(cookies) > 0:
            self._cookies.update(cookies)


    def set_method(self, method) -> 'Request':
        method = method.lower()

        if method not in self._allowMethods:
            raise TypeError

        self._method = method

        return self


    @property
    def method(self) -> str:
        return self._method


    def set_url(self, url) -> 'Request':
        self._url = url
        return self


    @property
    def url(self) -> str:
        return self._url


    @property
    def all(self) -> tuple:
        '''
        所有header和payload字典
        :return: dict
        '''
        return (self._url, self._method, self._headers, self._payload)


    @property
    def headers(self) -> dict:
        return self._headers


    def get_header(self, key: str) -> str or None:
        '''
        获取header的单个值
        :param key: header key
        :return: string
        '''
        return self._headers.get(key)


    def set_header(self, key: str, value) -> 'Request':
        '''
        设置header选项
        :param key: string
        :param value: string
        :return: self
        '''
        self._headers[key] = value
        return self


    def delete_header(self, key: str):
        '''
        删除header选项
        :param key: string
        :return: self
        '''
        del self._headers[key]
        return self


    @property
    def payload(self) -> dict:
        return self._payload


    def set_payload(self, key, value):
        self._payload[key] = value
        return self


    def get_payload(self, key):
        return self._payload.get(key)


    def delete_payload(self, key):
        del self._payload[key]
        return self


    @property
    def cookies(self) -> dict:
        return self._cookies


    def get_cookie(self, key: str):
        return self._cookies.get(key)


    def set_cookie(self, key: str, item: str):
        self._cookies[key] = item


    def delete_cookie(self, key: str):
        del self._cookies[key]


class Response(object):
    _actuator = None
    _request = None

    _encoding = 'utf-8'


    def __init__(self, request: Request) -> None:
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
            self._response = getattr(self._actuator, self._request.method)(self._request.url,
                                                                           headers=self._request.headers,
                                                                           **payload)
        except requests.exceptions.RequestException as e:
            print(e.strerror)
            raise e

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
    request = Request('http://baidu.com', 'get', {'host': '192.168.226.63'}, {'name': 'test'})
    request.set_method('POST')
    print(request.all)
