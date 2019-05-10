# coding=utf8

'''
Created on 2019��5��10��

@author: Administrator
'''
#1.元组基础
#1.元组创建
tup1 = ('physics','chemistry',1997,2000)
tup2 = (1,2,3,4,5);
tup3 = ("a","b","c","d")
#空元组
tup4 = ()
#注意：一个元素时，后面用 逗号 分隔
tup5 = (4,)

#2.访问元组元素
#单个
print(str(tup1[0]))
#遍历
print("遍历元组tup1: ",str(tup1))
#元组截取
print(str(tup1[1:3]))

#3.修改元组
#注意：元组中的元素不允许修改，但我们可以对元组进行连接组合

tup6 = tup1+tup2
print("元组6遍历: ",str(tup6))

#4.删除元组
#注意：元组中的元素值是不允许删除的，但我们可以使用del删除整个元组

del tup1
print("元组tup1被删除");

#2.元组的运算

print(len(tup2))
tup7 = tup2+tup3
print(3 in (tup3))
#迭代打印
for x in tup3:print(str(x))

#元组索引，截取
print(tup3[1])
print("打印倒数第二个元组元素： ",str(tup3[-2]))
print("截取倒数第二个元素之后的所有元组元素： ",str(tup3[-2:]))

#3.无关闭分隔符
#默认为元组
x,y = 1,2
print("Value of x,y: ",x,y)

#4.内置函数
tup1 = (1,2)
tup8 = (2,3,"hello")

print("tup1 长度： ",len(tup1))
print("tup1 元素中的最大值",max(tup1))
#注意混合类型的元组不能进行元素比较
#print("tup8 元素中的最大值",max(tup8))
print("tup1 中的最小值： ",min(tup1))
#5.将list转换为元组
num_list = [1,2,3,4]
print(str(tuple(num_list)))




