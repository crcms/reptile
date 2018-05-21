# -*- coding: utf-8 -*-

'''

下载器管理

'''

from reptile.download._request import Request


class Main(object):
    _request = Request()
    _actuator = None
    _url = None

    def __init__(self, url):
        # print({'x':1,'y':2})
        print(self._header.all())


if __name__ == '__main__':
    Main()
