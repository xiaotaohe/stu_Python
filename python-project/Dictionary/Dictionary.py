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
#1.字典内置函数&方法
print(len(rep_test))
print(str(rep_test))
print(type(rep_test))
temp_dict = {'Name': 'Zara', 'Age': 7};
#2.dic.copy()拷贝
    #1.浅拷贝：引用对象
    #2.浅拷贝：深拷贝父类对象（一级目录），子对象（二级目录）不拷贝

dict1 =  {'user':'runoob','num':[1,2,3]}
dict2 = dict1#引用与赋值的区别
dict3 = dict1.copy()#2.浅拷贝
#修改，看结果
dict1['user'] = 'root'
dict1['num'].remove(1)

print(dict1)
print(dict2)
print(dict3)

#3.dict.fromkeys(seq[,val])
#创建新字典，以序列seq中元素做字典的键，val作为字典所有键值对应的初始值
seq = ('google','runoob','taobao')
from_dict = {}
from_dict = from_dict.fromkeys(seq)
print("%s "% str(from_dict))
print(from_dict)
from_dict = from_dict.fromkeys(seq,10)
print(from_dict)

#4.判断是否存在
#python3.x 使用dict.__contains__(key)
#前期版本使用dict.has_key(key)
flag = from_dict.__contains__('goo')
print(flag)

#5.dict.items()
#遍历返回遍历的(key,value)元组数组
print(str(from_dict.items()))
tup = []
tup = from_dict.items()
print(tup)

#6.dict.update(dict2)
#将元组2中的键值对更新到dict中,追加方式
from_dict.update(dict1)
print(from_dict)

#7.dict.values()
#返回字典中的所有值
print(from_dict.values())
print(type(from_dict.values()))

#8.dict.pop(key.[,default])
#删除字典给定key值的键值对，返回被删除的值
print(from_dict.pop("taobao"))
print(from_dict)
from_dict.update({"baidu":123,})
print(from_dict)

#9.dict.popitem()
#随机返回并删除字典中的一对键值对
print(from_dict.popitem())
print(from_dict)

