'''
Created on 2019年5月9日

@author: Administrator
'''
# -*-coding:utf-8-*-
from ctypes import string_at
from test.test_keywordonlyarg import mixedargs_sum

#1.学习list基础
#尝试打印中文字符串
print("你好！")

print("what's your name?\nTom")

#下面是关于list的使用

#1.创建list

number_list = [1,3,5,9]
# print("number_list:"+str(number_list))
# 
string_list = ["abc","bbc","python"]
# print("string_list:"+str(string_list))
# 
# #多种类型的list（python的强大之处）
mixed_list = ["abc","bbc",2,12]
# print("mixed_list:"+str(mixed_list))


second_num = number_list[1]
third_string = string_list[2]
fourth_mixed = mixed_list[3]

print("second_num:{0} third_str:{1} fourth_mix:{2}".format(second_num,third_string,fourth_mixed))


#元素更新
number_list[1] = 10;
print("change number_list after: "+str(number_list))

#删除元素
del number_list[1]
print("del number_list after: "+str(number_list))

#2.学习list的脚本
#1.获取长度
print(len(number_list))
#2.组合
num_list = [1,2,3]
num_list1 = [4,5,6]
print("num_list+num_list2: ",str(num_list+num_list1))
#3.重复
string1_list = ['hello']*4
print("strig1_list: ",string1_list)
#4.判断某元素是否在list中
flag = 5 in num_list
print(flag)
#5.跌代
for x in [1,2,3]:print(x)


#3.学习list的截取
#读取第二个元素
print (str(num_list[1]))
#读取倒数第一个元素
print(str(num_list[-1]))
#截取从第二个元素之后的列表
print(str(num_list[1:]))
num_list2 = num_list1[1:]
print("截取num_list1第二个之后及第个元素的列表:",str(num_list2))


#4.学习一些列表中的方法
print(len(num_list))#获取列表长度
print(max(num_list))#获取列表中的最大值
print(min(num_list))