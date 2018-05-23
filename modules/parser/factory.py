# -*- coding: utf-8 -*-

'''



'''

from modules.parser.html import Html
from modules.parser.json import Json


class Factory(object):

    @staticmethod
    def factory(type, Response):
        return {
            'html': Html(Response),
            'json': Json(Response)
        }[type]
