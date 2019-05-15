# coding=utf8
'''
Created on 2019年5月15日

@author: Administrator
'''
#输入输出
str1 = input("enter a string: ")
str2 = input("enter another string: ")

print("str1: "+str1+",str2: "+str2)
print("str1: {0},str2: {1}".format(str1,str2))


#文件的输入输出
out_put1 = ('''
I love leaning python.
becuse python is fun,
and also easy to use
''')
#将字符串写入文件
f = open("sentences.txt","w")
f.write(out_put1)
f.close()
#将文件的内容读出
f = open("sentences.txt","r")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()

    