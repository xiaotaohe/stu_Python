#coding=utf8
'''
Created on 2019��5��12��

@author: Administrator
'''
#python函数的学习
#python没有分号做分隔符
#以table键分隔
#1.无返回值的函数
def say_hi():
    print("hi")
say_hi()
say_hi()

def print_sum_two(a,b):
    c = a + b
    print("{0} + {1} = ".format(a,b),c)
print_sum_two(1,2)
print_sum_two(2,2)

def hello_str(str):
    print("hello "+str+"!")
hello_str("china")
hello_str("python")

#2.有返回值的函数
def repeat_str(str,times):
    repeates = str*times
    return repeates
repeated_string = repeat_str("Happy Birthday!", 4)
print(repeated_string)

#3.全局变量 
x = 66
#1.全局变量与局部变量
def fun(x):
    print("x is: "+str(x))
    x = 5
    print("change local x to: ",str(x))
fun(x)
print("x is still: ",str(x))

#2.在函数内部使用全局变量
def fun1():
    global x
    print("x is: "+str(x))
    x = 6
    print("change local x to: ",str(x))
fun1()
print("x is still: ",str(x))
#3.缺省参数
def test_que(str = "hehe",times = 1):
    repeates = str*times
    return repeates
repeated = test_que("hello world!")
print(repeated)
repeated = test_que("hello world!",4)
print(repeated)
repeated = test_que()
print(repeated)
