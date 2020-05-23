# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:20:54 2020

@author: User
"""

#先建立一個空的數學成績清單
math=list()

#詢問人數
num=input("全班人數:")
num=int(num)

#將姓名,成績放入[成績清單]
for i in range(num):
    name=input("學生姓名:")
    score=input("數學成績:")
    score=int(score)
    
    #再放入清單之前先建立一個學生的[個人小清單]
    student=list()
    #將名字,成績,放入個人清單
    student.append(name)
    student.append(score)
    
     #將[個人清單]放入[數學成績清單]
    math.append(student)
    
#顯示數學成績清單
print("數學成績單:",math)
###########################################################


    
    
    
    
    