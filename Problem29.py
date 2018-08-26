# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:50:37 2018

@author: Freek
"""

temp = set()
for i in range(2,101):
    for j in range(2,101):
        temp.add(i**j)
        
print('%d distinct terms generated' %len(temp))