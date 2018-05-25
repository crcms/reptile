# -*- coding: utf-8 -*-

'''



'''

from modules.download.request import Request
from modules.download.response import Response
from modules.parser.parse import Parse
from modules.store.store import Store
from modules.url.manage import Url
from time import sleep


class Main(object):

    def start(self, url: str):

        url_manage = Url()
        url_manage.adds(set([url]))
        store = Store()
        while (True):

            url_object = url_manage.get_url()

            if url_object is None:
                break

            response = Response(Request(url_object['url']))

            parse = Parse.factory('html', response)

            url_manage.adds(parse.urls())

            store.update(url_object['_id'], {'content': parse.content()})

            print('已抓取的URL' + url_object['url'] + '(' + str(url_object['_id']) + ')')

if __name__ == '__main__':
    Main().start('http://thinkphp.cn')
