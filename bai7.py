# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:26:57 2024

@author: Admin
"""

a=float(input("Nhập độ dài cạnh a:"))
b=float(input("Nhập độ dài cạnh b:"))
c=float(input("Nhập độ dài cạnh c:"))

if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print("Đây là một tam giác đều")
    elif a==b or b==c or c==a:
        print("Đây là một tam giác đều")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("Đây là tam giác vuông")
    elif a**2>b**2+c**2 or b**2>c**2+a**2 or c**2>b**2+a**2:
        print("Đây là một tam giác tù")
    else:
        print("Đây là một tam gác thường")
else: 
    print("Đây không phải là một tam giác")


