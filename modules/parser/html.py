# -*- coding: utf-8 -*-

'''



'''

from modules.parser.parse import Parse
from bs4 import BeautifulSoup
import re

class Html(Parse):
    _beautifulSoup = None

    def __init__(self,Response):
        super.__init__(Response)
        self._beautifulSoup = BeautifulSoup(self._response.responseText, 'html5lib')


    def urls(self):
        urls = self._beautifulSoup.find_all('a', href=re.compile(r'^/[\w]+/[\w]+.html$'))

        # x = self._beautifulSoup.find_next('a',href=compile(r'/[\w]+/[\w]+.html'))
        # print(x)

        pattern = re.compile(r'href=["]?(/[\w]+/[\w]+.html)["]?')

        return ['http://thinkphp.cn' + url.attrs.get('href') for url in urls]

    def content(self):
        return self._response.responseText


if __name__ == '__main__':
    from modules.download.request import Request
    from modules.download.response import Response
    from modules.parser.factory import Factory

    currentRequest = Request('http://thinkphp.cn')
    currentResponse = Response(Request)

    parser2 = Factory.factory('html',currentResponse)
    print(parser2)