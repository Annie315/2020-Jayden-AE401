# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:11:42 2020

@author: User
"""

studentName=[]

scores=[]

num=int(input("請輸入學生人數:"))

for i in range(num):
    
    name=input("請輸入學生姓名")
    studentName.append(name)
    
    a=int(input("請輸入分數"))
    scores.append(a)

print(scores)

############################
sum=0
for i in range(num):
    sum=sum+scores[i]

avg=sum/num
print("平均分數:",avg)

############################

highest=0
lowest=100

for i in range(num):
    if scores[i]>highest:
        highest=scores[i]
        h=i
    if scores[i]<lowest:
        lowest=scores[i]
        l=i
print("最高分:",highest,"是:",studentName[h])
print("最低分:",lowest,"是:",studentName[l])