# -*- coding: utf-8 -*-

'''

爬虫调度器

'''

from crcms_spider.base.manager import Url
from crcms_spider.base.store import Store
from crcms_spider.base.downloader import Request, Response
from crcms_spider.base.parser import Parse
from configparser import ConfigParser
from crcms_spider.models.data import Data
from crcms_spider.base.manager import AbstractUrl


class Dispatch(object):

    def run(self, config: ConfigParser, url_manage: Url, store: AbstractUrl, parse: Parse):

        while (True):

            url_object = url_manage.get_url()

            if url_object is None:
                break
            response = parse(Response(
                Request(url_object['url'])
            ), dict(config['parse']))

            url_manage.adds(response.urls())

            url_object = store.update(url_object,
                                      content=response.content(),
                                      title=response.title(),
                                      )

            print('已抓取的URL' + url_object['url'] + '(' + str(url_object.id) + ')')


if __name__ == '__main__':
    import configparser, os

    config = configparser.ConfigParser()
    config.read(os.getcwd() + '/../../config.ini')

    url = Url(Data, dict(config['manage']))
    # print(dict(config['manage']))
    url.adds(set([config['manage']['first_url']]))

    store = Store()

    parse = Parse.factory(dict(config['parse']))

    Dispatch().run(config, url, Data, parse)
