# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:49:30 2018

@author: Freek
"""


from functools import reduce
i = 100
j = str(reduce(lambda x,y: x*y, range(1,i+1)))

temp = []
for n in j:
    temp.append(int(n))
print('Sum of digits in the number 100!: %d' %sum(temp))