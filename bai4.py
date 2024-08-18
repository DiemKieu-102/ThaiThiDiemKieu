# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:32:59 2024

@author: Admin
"""

a=float(input("a:"))
b=float(input("b:"))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình cô nghiệm")
else:
    x=-b/a
    print("Phương trình có một nghiệm x", x) 
    