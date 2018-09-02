# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:33:23 2018

@author: Freek
"""

import decimal
decimal.getcontext().prec = 101

def square_root(n):
    return sum(decimal.Decimal(n).sqrt().as_tuple()[1][0:100]), len(decimal.Decimal(n).sqrt().as_tuple()[1])

temp = []
for i in range(1,101):
    sum_sqrt_i, len_sqrt_i = square_root(i)
    if len_sqrt_i > 2:
        temp.append(sum_sqrt_i)
    
print('Total of sum of first 100 decimal digits of irrational square roots of first 100 natural numbers is: %d' %sum(temp))