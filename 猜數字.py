# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:36:48 2020

@author: User
"""


#招喚模組/計入模組
import random

#使用它/呼叫它
num=random.randint(1,10)

#輸入
a=input("請輸入數字:")
#強制轉型
a=int(a)

#判斷
if a==num:
    print("恭喜猜對了")
else:
    print("猜錯了")
    
    