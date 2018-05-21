# -*- coding: utf-8 -*-

'''

request请求头组装处理

'''


class Request(object):
    _headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    _contents = {

    }

    def __init__(self, **kwargs):
        '''
        header设置
        :param kwargs: dict header选项
        '''
        self._headers.update(kwargs)

    def all(self):
        '''
        所有header数组
        :return: dict
        '''
        return self._headers

    def get(self, key):
        '''
        获取header的单个值
        :param key: header key
        :return: string
        '''
        return key

    def set(self, key, value):
        '''
        设置header选项
        :param key: string
        :param value: string
        :return: self
        '''
        self._headers[key] = value
        return self

    def delete(self, key):
        '''
        删除header选项
        :param key: string
        :return: self
        '''
        del self._headers[key]
        return self


# if __name__ == '__main__':
#     header = Header()
#     header.get_headers['x'] = 123
#     print(header.get_headers)
