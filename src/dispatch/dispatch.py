# -*- coding: utf-8 -*-

'''

爬虫管理（调度）

'''

from src.download.download import Download
from src.parse.parse import Parse
from src.manage.url import Url

class Dispatch(object):

    _url = None
    _parse = None
    _download = None

    def __init__(self):
        self._url = Url()
        self._parse = Parse()
        self._download = Download()


    def handle(self):

        init_url = 'http://www.thinkphp.cn'


        while True:

            content = self._download.handle(init_url)

            print('正在抓取的URL' + init_url)

            urls,content = self._parse.handle(content)

            self._url.add_urls(set(urls))

            # store
            if content:
                fp = open('./contents/' + init_url.split('/')[-1:].pop(),'w',encoding='utf-8')
                fp.write(content)
                fp.close()

            if self._url.complete_url_length() >= 500 or not self._url.has_url():
                break

            # 追加URL
            init_url = self._url.get_one()

if __name__ == '__main__':
    manage = Dispatch()
    manage.handle()
