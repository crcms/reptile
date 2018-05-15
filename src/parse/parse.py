# -*- coding: utf-8 -*-

'''

Html 解析

'''

from bs4 import BeautifulSoup
import re


class Parse(object):
    # _content = None
    _beautifulSoup = None

    def __init__(self):
        pass

    def handle(self, content):
        # self._set_content(content)
        self._beautifulSoup = BeautifulSoup(content, 'html5lib')

        return (self.parse_url(), self.parse_content())

    def parse_url(self):
        urls = self._beautifulSoup.find_all('a', href=re.compile(r'^/[\w]+/[\w]+.html$'))

        # x = self._beautifulSoup.find_next('a',href=compile(r'/[\w]+/[\w]+.html'))
        # print(x)

        pattern = re.compile(r'href=["]?(/[\w]+/[\w]+.html)["]?')

        return ['http://thinkphp.cn' + url.attrs.get('href') for url in urls]

    def parse_content(self):
        '''
        content
        :return:
        '''
        #,lambda tag : tag.has_class('detail-bd')
        x = self._beautifulSoup.find('div',class_='detail-bd')
        if x:
            return x.prettify()

        return x

    def _set_content(self, content):
        self._content = content

# if __name__ == '__main__':
