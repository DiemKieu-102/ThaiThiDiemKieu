# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:50:55 2024

@author: Admin
"""

import math
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
#Thực hiện kiểm tra
detal = b**2 - 4*a*c
if detal == 0:
    x= -b / 2*a
    print("Phương trình có nghiệm kép là: ", x )
elif detal < 0:
    print("Phương trình vô nghiệm")
else:
    x1=(-b + math.sqrt(detal))/(2*a)
    x2=(-b - math.sqrt(detal))/(2*a)
    print("Phương trình có hai nghiệm phân biệt là: ")
    print("x1", x1)
    print("x2", x2)

    
    
