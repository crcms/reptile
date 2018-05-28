# -*- coding: utf-8 -*-

'''



'''

import re

# x = re.compile(r'^http://www\.ruanyifeng\.com/blog/[\w\/]+\.html$',re.I)
#
# y = re.search(x,'http://www.ruanyifeng.com/blog/2018/05/weekly-issue-4.html')
# print(y)

# x = re.search(r'abc\.\.com','abc..com')
# print(x.group())

# x = re.search(r'http://baidu\.com','gfdsafdahttp://baidu.com')
# print(x.group())


x = re.compile(r'^http://www\.ruanyifeng\.com/blog/[\w\-/]+\.html$',re.I)

y = re.search(x,'http://www.ruanyifeng.com/blog/2018/05/weekly-issue-4.html')
print(y)