# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:01:53 2020

@author: User
"""


import turtle

A = turtle.Turtle() #生成烏龜

C = turtle.Screen() #生成畫布

C.title("my window")

C.bgcolor("black")

A.color("yellow")
A.shape("turtle")
A.pensize(6)

i=0

while i<1:
    A.left(45)
    A.forward(100)
    i=i+1
    
turtle.done()