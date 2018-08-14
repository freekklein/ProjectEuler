# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:20:38 2018

@author: Freek
"""

temp = []
temp2 = []
max_number = 500

for i in range(1,1000):
    temp.append(i)
    temp2.append(sum(temp))
    
#print(temp2)

for i in temp2:
    temp3 = []
    for j in range(1,1000):
        if i % j == 0:
            temp3.append(j)
    if len(temp3)>max_number:
        print('Triangle Number %d with %d divisors' %(i,len(temp3)))
        break