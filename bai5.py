# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:49:51 2024

@author: Admin
"""

X =float(input("Nhập độ dài đoạn đường đến trường (m)"))
if X <300:
    print("Đường đến trường quá gần. Thôi đi bộ")
elif X>1200:
    print("Đường đến trường quá xa. Thôi đi xe máy")
elif X>= 300 and X <= 700:
    print("Đường đến trường không xa. Thôi đi xe đạp")
else:
    print("Không xác định được")
