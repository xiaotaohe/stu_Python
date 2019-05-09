'''
Created on 2019年5月9日

@author: Administrator
'''
# -*-coding:utf-8-*-
from ctypes import string_at
from test.test_keywordonlyarg import mixedargs_sum

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
