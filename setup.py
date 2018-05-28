# -*- coding: utf-8 -*-

'''

系统启动

'''

from setuptools import setup, find_packages

setup(
    name='crcms_spider',
    version='0.0.1',
    author='simon',
    author_email='crcms@crcms.cn',
    description='A sample reptile',
    long_description='''
        
    ''',
    # 所有模块加载
    # packages=find_packages(),
    # 当项目都是.py文件时使用py_modules
    py_modules=find_packages(),
    # 需要的依赖包
    install_requires=[
        'requests', 'bs4', 'urllib', 'pymongo'
    ],
    # 程序命令生成
    entry_points='''
    [console_scripts]
    run = reptile:main
    '''
)
