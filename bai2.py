# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:21:46 2024

@author: DiemKieu
"""
GPA =float(input("Nhập GPA (a):"))
if  GPA < 3.5:
    print("Học lực kém")
elif 3.5 <= GPA < 5.0:
    print("Học lực yếu")
elif  5.0 <= GPA <7.0:
    print("Học lực trung bình")
elif 7.0 <= GPA <8.0:
    print("Học lực khá")
elif 8.0 <= GPA <9:
    print("Học lực giỏi")
elif 9.0 <= GPA <=10:
    print("Học lực xuất sắc")
else:
    print("Không xác định")
      
