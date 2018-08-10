# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:45:30 2018

@author: EL11LV
"""

temp = []
for i in range(100,1000):
    for j in range(100,1000):
        if int(str(i*j)[::-1]) == i*j:   # change int to string to reverse order
            temp.append(i*j)
            
print(max(temp))