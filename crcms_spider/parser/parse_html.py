# -*- coding: utf-8 -*-

'''



'''

import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from crcms_spider.base.parser import Parse
from crcms_spider.base.downloader import Response


class Html(Parse):
    _beautifulSoup = None


    def __init__(self, response: Response, config: dict) -> None:
        '''
        :param response:
        :type Response
        '''
        super().__init__(response, config)
        self._beautifulSoup = BeautifulSoup(self._response.responseText, 'html5lib')


    def urls(self) -> set:
        '''

        :return: set
        '''
        # urls = self._beautifulSoup.find_all('a', href=re.compile(self._config['url_pattern']))
        urls = self._beautifulSoup.find_all('a', href=re.compile(r'{match}'.format(match=self._config['url_pattern'])))

        parse = urlparse(self._response.request.url)

        return set([parse.scheme + '://' + parse.netloc + '/' + url.attrs.get('href').lstrip('/') if (
                url.attrs.get('href').find('://') == -1) else url.attrs.get('href') for url in urls])


    def content(self) -> str:
        '''

        :return: str
        '''
        return self._response.responseText


    def title(self) -> str:
        try:
            return self._beautifulSoup.title.string
        except AttributeError:
            return ''
