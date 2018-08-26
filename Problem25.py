# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:23:03 2018

@author: Freek
"""

temp = []
temp.append(1)
temp.append(1)

while len(str(temp[-1]))<1000:
    temp.append(temp[-1]+temp[-2])
    
print('Index of first term in Fibonacci sequence to contain 1000 digits: %s' %str(temp[-1])[0])