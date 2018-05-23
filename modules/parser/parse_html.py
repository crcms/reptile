# -*- coding: utf-8 -*-

'''



'''

import re
from bs4 import BeautifulSoup
from modules.parser.parse import Parse
from urllib.parse import urlparse
from modules.download.response import Response


class Html(Parse):
    '''
    :type BeautifulSoup
    '''
    _beautifulSoup = None

    def __init__(self, response: Response) -> None:
        '''
        :param response:
        :type Response
        '''
        super().__init__(response)
        self._beautifulSoup = BeautifulSoup(self._response.responseText, 'html5lib')

    def urls(self) -> set:
        '''

        :return: set
        '''
        urls = self._beautifulSoup.find_all('a', href=re.compile(r'^/[\w]+/[\w]+.html$'))

        # x = self._beautifulSoup.find_next('a',href=compile(r'/[\w]+/[\w]+.html'))
        # print(x)

        parse = urlparse(self._response.request.url)

        # pattern = re.compile(r'href=["]?(/[\w]+/[\w]+.html)["]?')

        return set([parse.scheme + '://' + parse.netloc + '/' + url.attrs.get('href').lstrip('/') for url in urls])

    def content(self) -> str:
        return self._response.responseText


if __name__ == '__main__':
    from modules.download.request import Request
    from modules.download.response import Response

    # from modules.parser.factory import Factory

    currentRequest = Request('http://thinkphp.cn')
    currentResponse = Response(currentRequest)

    parse = Parse.factory('html', currentResponse)
    print(parse.urls())

    # parser2 = Factory.factory('html',currentResponse)
    # print(parser2)
