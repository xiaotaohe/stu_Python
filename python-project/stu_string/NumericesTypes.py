'''
Created on 2019年5月9日

@author: Administrator
'''
import sys

#创建变量a
a  = 3
b = 4
#浮点型变量
c = 5.66
d = 8.0
#复数
e = complex(c,d)
f = complex(float(a),float(b))

#获取变量a的类型
print("a is type:",type(a))
print("c is type:",type(c))
print("e is type:",type(e))

print(a+b)
print(d/c)

print(b/a)

#双斜杠除，向下约减
print(b//a)
#复数
print(e)
print(e+f)

#浮点数通过系统命令获取它的数据范围

print(sys.float_info)
