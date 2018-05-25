# -*- coding: utf-8 -*-

'''



'''
# from bs4 import BeautifulSoup
#
# import sys
# print(sys.path)


class Test(object):

    x = 10

    def func(self,abc):
        print(abc+'123')




class Py(object):


    y = 1


    def __init__(self):
        self.test = Test()

    def xs(self):
        pass

    def __getattr__(self, item):

        if hasattr(self.test,item):

            return getattr(self.test,item)




py = Py()
x = py.func
x('ssss')
# py.x