# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:55:55 2018

@author: Freek
"""

temp = []
numb = 1000

for i in range(1,numb+1):
    temp.append(i**i)
    
#print(sum(temp))
print(sum(temp) % int(1e+10))
