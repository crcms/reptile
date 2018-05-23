# -*- coding: utf-8 -*-

'''

request请求头组装处理

'''


class Request(object):

    _headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    _payload = {
    }

    _method = 'get'

    _allowMethods = set(['get', 'post', 'delete', 'options', 'head', 'put', 'update'])

    _url = None

    def __init__(self, url, method='get', headers={}, payload={}, **kwargs):
        '''
        header设置
        :param kwargs: dict header选项
        '''

        self.set_url(url).set_method(method)

        if len(headers) > 0:
            self._headers.update(headers)

        if len(payload) > 0:
            self._payload.update(payload)

    def set_method(self, method):
        method = method.lower()

        if method not in self._allowMethods:
            raise TypeError

        self._method = method

        return self

    @property
    def method(self):
        return self._method

    def set_url(self, url):
        self._url = url
        return self

    @property
    def url(self):
        return self._url

    @property
    def all(self):
        '''
        所有header和payload字典
        :return: dict
        '''
        return (self._url, self._method, self._headers, self._payload)

    @property
    def headers(self):
        return self._headers

    def get_header(self, key):
        '''
        获取header的单个值
        :param key: header key
        :return: string
        '''
        return self._headers.get(key)

    def set_header(self, key, value):
        '''
        设置header选项
        :param key: string
        :param value: string
        :return: self
        '''
        self._headers[key] = value
        return self

    def delete_header(self, key):
        '''
        删除header选项
        :param key: string
        :return: self
        '''
        del self._headers[key]
        return self

    @property
    def payload(self):
        return self._payload

    def set_payload(self, key, value):
        self._payload[key] = value
        return self

    def get_payload(self, key):
        return self._payload.get(key)

    def delete_payload(self, key):
        del self._payload[key]
        return self

if __name__ == '__main__':
    request = Request('http://baidu.com','get',{'host':'192.168.226.63'},{'name':'test'})
    request.set_method('POST')
    print(request.all)
