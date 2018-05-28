# -*- coding: utf-8 -*-

'''



'''

import importlib
from abc import ABCMeta, abstractmethod
from crcms_spider.base.downloader import Response
from configparser import ConfigParser


class Parse(metaclass=ABCMeta):
    _response = None
    _config = None


    def __init__(self, response: Response, config: dict) -> None:
        '''
        :param response:
        :type Response
        '''
        self._response = response
        self._config = config


    @abstractmethod
    def urls(self) -> set:
        '''
        返回内容中所有解析的需要抓取的惟一URL
        :return: set
        '''
        pass


    @abstractmethod
    def content(self) -> str:
        '''
        返回指定区域内容
        :return:
        '''
        pass


    @staticmethod
    def factory(config: dict) -> 'Parse':
        '''
        子类工厂
        :param type:
        :type str
        :param response:
        :type Response
        :return: Parse()
        '''

        type = config['type'] or 'html'
        module = config['module'] or 'crcms_spider.parser.parse_html'

        parse = importlib.import_module(module)

        parse = getattr(parse, type.capitalize())
        if parse is None:
            raise TypeError

        return parse


if __name__ == '__main__':
    import os

    config = ConfigParser()
    path = os.fspath(os.getcwd() + '/../../config.ini')
    config.read(path)

    print(config['parse']['module'])
    exit()

    print(Parse.factory(config, 'x'))
