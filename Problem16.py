# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 07:42:11 2018

@author: Freek
"""

power = 1000
number = 2**power

temp = []
for i in str(number):
    temp.append(int(i))
    
print('Sum of digits of the number 2 to the power %d is %d' %(power,sum(temp)))