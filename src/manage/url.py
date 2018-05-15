# -*- coding: utf-8 -*-

'''

URL管理器

'''


class Url(object):
    _urls = set([])
    _complete_urls = set([])

    def __init__(self):
        pass

    def add_urls(self, urls):
        '''
        添加需要抓取的URL
        :param urls:
        :return: self
        '''

        if not isinstance(urls, set):
            raise TypeError

        self._urls.update(urls)

        return self


    def get_one(self):
        '''
        返回一个需要抓取的URL
        :return: string
        '''
        url = self._urls.pop()
        self._complete_urls.add(url)
        return url


    def urls(self):
        '''
        返回所有需要抓取的URL
        :return:set
        '''
        return self._urls


    def complete_urls(self):
        '''
        返回所有抓取完成的URL
        :return: set
        '''
        return self._complete_urls


    def has_url(self):
        '''
        判断是否存在需要抓取的URL
        :return: Bool
        '''
        return len(self._urls) > 0


    def complete_url_length(self):
        '''
        返回已经抓取的URL长度
        :return: int
        '''
        return len(self._complete_urls)
