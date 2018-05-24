# -*- coding: utf-8 -*-

'''



'''

import importlib
from abc import ABCMeta, abstractmethod
from modules.download.response import Response


class Parse(metaclass=ABCMeta):

    _response = None

    def __init__(self, response: Response) -> None:
        '''
        :param response:
        :type Response
        '''
        self._response = response

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
    def factory(type: str, response: Response):
        '''
        子类工厂
        :param type:
        :type str
        :param response:
        :type Response
        :return: Parse()
        '''
        parse = importlib.import_module('parse_' + type, 'modules.parser')

        parse = getattr(parse, type.capitalize())(response)
        if parse is None:
            raise TypeError

        return parse


if __name__ == '__main__':
    print(Parse.factory('html', 'x'))
