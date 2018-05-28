# -*- coding: utf-8 -*-

'''



'''
from configparser import ConfigParser
import os

# config = ConfigParser()
# config.read(os.getcwd() + '/../config.ini')
# print(config['parse']['url_pattern'])
# x = '%r'%config['parse']['url_pattern']
# print(x)
# # string = '12\n3'
# # print(r'12\n3')
# # print(r'' + string + '')
#
# x = "r'123'"
# print(x)


# x = '123'
# print(x.find('10'))

string = 'sxxx'

print(r'{match}'.format(match=string))