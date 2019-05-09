# coding=utf8
'''
Created on 2019��5��9��

@author: Administrator
'''
import os
'''
os.getcwd()方法用来获取当前文件路径
'''
import requests
print(os.getcwd());
r = requests.get("http://www.baidu.com")
'''
获取网页对象
'''

print(r.url)
'''
获取url的编码方式
'''

print(r.encoding)
print(r.text)
