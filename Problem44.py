# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:38:57 2018

@author: Freek
"""

#import time
temp = []

for i in range(1,3050):
    temp.append(i*(3*i-1)/2)
#print(temp)
temp_unique = set(temp)

for i in temp_unique:
    for j in temp_unique:
        if i+j in temp_unique:
            if j-i in temp_unique:
                print('D:', j-i)
                print('j:',temp.index(i)+1)
                print('k:',temp.index(j)+1)