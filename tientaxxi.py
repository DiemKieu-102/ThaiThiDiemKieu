# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:57:34 2024

@author: Admin
"""

def calculate_taxi_fare(km):
    if km <= 1:
        fare = 20
    elif km <= 3:
        fare = 20 + (km - 1) * 13
    elif km <= 8:
        fare = 20 + 2 * 13 + (km - 3) * 12
    else:
        fare = 20 + 2 * 13 + 5 * 12 + (km - 8) * 10
    if fare > 100:
        fare *= 0.92
    return fare
km = float(input("Nhập số km đã đi: "))
total_fare = calculate_taxi_fare(km)
print(f"Số tiền phải trả là: {total_fare:.2f}k")