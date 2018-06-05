# -*- coding: utf-8 -*-

'''



'''

from scrapy import Spider
from bs4 import BeautifulSoup
import re
from scrapy.http.response.html import HtmlResponse

class ThinkPHP(Spider):

    name = 'thinkphp'

    start_urls = ['http://thinkphp.cn']

    #scrapy.http.response.html.HtmlResponse
    def parse(self, response:HtmlResponse):
        pass
        # / html / body / div[3] / div[3] / div[3] / div[2] / ul / li[1] / a
        # papers = response.xpath('')
        # print(response.body_as_unicode())
        # exit()
        # response.encoding = 'utf-8'
        # beautifulSoup = BeautifulSoup(response.text, 'html5lib')
        #
        # urls = beautifulSoup.find_all('a', href=re.compile(r'^/[\w]+/[\w]+.html$'))
        # print(urls)
