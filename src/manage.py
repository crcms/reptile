# -*- coding: utf-8 -*-

'''

爬虫管理（调度）

'''

from src.download import Download
from src.parse import Parse
from src.url import Url

class Manage(object):

    _url = None
    _parse = None
    _download = None

    def __init__(self):
        self._url = Url()
        self._parse = Parse()
        self._download = Download()


    def handle(self):

        init_url = 'http://thinkphp.cn'

        content = self._download.handle(init_url)

        urls = self._parse.handle(content)


if __name__ == '__main__':
    manage = Manage()
    manage.handle()
