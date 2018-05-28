# -*- coding: utf-8 -*-

'''



'''

from configparser import ConfigParser
import os


config = ConfigParser()

# filename =
config.read(os.getcwd() + '/config.ini','UTF-8')
print(type(config))
print(dict(config['z']))
# print(type(config))
# print(os.fspath('/b/c'))