# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 21:47:04 2018

@author: Freek
"""

import time
factorials = [1,1,2,6,24,120,720,5040,40320,362880]

def fact_digits(n):
    temp = []
    for i in str(n):
        temp.append(factorials[int(i)])
    return sum(temp)

def fact_digits_loop(x):
    test = False
    chain = []
    chain.append(x)
    while test==False:
        x = fact_digits(x)
        if x not in chain:
            chain.append(x)
        else:
            test=True
    return chain

st = time.time()
for i in range(10,500000):
    chain = fact_digits_loop(i)
    if len(chain)==60:
        print('hello %d', i)
        break
    
print('It took %d seconds' %(time.time()-st))