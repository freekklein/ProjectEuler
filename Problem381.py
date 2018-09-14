# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:14:40 2018

@author: Freek
"""

from functools import reduce

def S(p):
    k = range(1,6)
    temp = []
    for i in [p-j for j in k]:
        if i == 0:
            temp.append(1)
        else:
            temp.append(reduce(lambda x,y: x*y, range(1,i+1)))
    return sum(temp) % p

def prime(p):
    test = 'Y'
    if p<3:
        test = 'Y'
    for i in range(2,p):
        if p%i==0:
            test = 'N'
    return test

temp2 = []
for i in range(5,int(1e+08)):
    if prime(i)=='Y':
        temp2.append(S(i))

print('S(p) = %d for 5 <= p < 1e+08' %sum(temp2))