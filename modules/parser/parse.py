# -*- coding: utf-8 -*-

'''



'''

from abc import ABCMeta, abstractmethod
from modules.parser.html import Html
from modules.parser.json import Json

class Parse(metaclass=ABCMeta):
    _response = None

    def __init__(self, Response):
        self._content = Response

    @abstractmethod
    def urls(self): pass

    @abstractmethod
    def content(self): pass

    @staticmethod
    def factory(type, Response):
        return {
            'html': Html(Response),
            'json': Json(Response)
        }[type]
