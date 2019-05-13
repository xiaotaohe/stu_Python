# coding=utf8
'''
Created on 2019��5��13��

@author: Administrator
'''
from audioop import getsample

suber = 50

#input 获取用户输入，input前面的int是指获取整形（int）
getse = int(input("inter to youreger: "))
print("guess input："+str(getse))

#stude if语句
def guess_num():
    num = 55
    getnum = int(input("inter to youreger: "))
    if num == getnum:
        print("you are right!")
        print("(but you do not win any prizes!)")
    elif num < getnum:
        print("No,the number is higher than taht")
    else:
        print("No,the number is a lower than that")
    print("done")
guess_num()

#stude for语句
for i in range(1,10):
    print(i)

#for循环遍历list
a_list = [1,2,3,4,5]
for i in range(0,5):
    print(str(a_list[i]))

#for循环遍历
a_dict = {"Tom":12,"Jerry":34,"Cathy":32}
for key,elem in a_dict.items():
    print(key,elem)

#猜数字小游戏
def guess():
    flag = 0
    sys_num = 12
    print("begin game!")
    for i in range(1,11):
        getnum = int(input("inter your number: "))
        if getnum == sys_num:
            flag = 1
            break
        elif getnum < sys_num:
            print("your num lower sys_num")
        else:
            print("your num higher sys_num")
    if flag == 1:
        print("you are right")
    else:
        print("time out ten,game over")
#函数调用
guess()
            
            
        
        
        
