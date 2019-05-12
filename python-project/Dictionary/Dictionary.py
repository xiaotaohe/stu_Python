# coding=utf8
'''
Created on 2019��5��12��

@author: Administrator
'''
#1.创建dictionary

phone_book = {"Tom":123,"Jerry":456,"Kin":789}
mixed_dict = {"Tom":"boy",11:23.6}

#访问
print("Tom phone number: "+str(phone_book["Tom"]))

#2.修改Diction
phone_book['Tom'] = 999
print("Tom phone number: "+str(phone_book["Tom"]))
#3.添加
phone_book["Kes"] = 888
print("Tom phone number: "+str(phone_book["Kes"]))

#4.删除
del phone_book['Tom']
print("after book: "+str(phone_book))

#5.清空
phone_book.clear()
print("Tom phone number: "+str(phone_book))

#6.删除整个Dictionary
del phone_book
#此时下面语句将报错
#print("Tom phone number: "+str(phone_book))

#7.字典中不能出现重复的元素
rep_test = {'name':'nb','age':5,'name':'nb'}
print("re_test: "+str(rep_test))
#重复被去掉，不能同一个key出现多次

#8.key必须是immutable(不可变)
#可以用数字，字符串，元组充当key，但是不能用列表（list）
#使用list就会出错
#list_dic = {['name']:'jion','age':13}
#使用元组没问题
tup_dic = {('name'):'jion','age':13}

#dictionary方法学习



