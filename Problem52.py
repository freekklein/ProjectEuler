# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 17:59:04 2018

@author: Freek
"""

def same_digit(n):
    if ''.join(sorted(str(n))) == ''.join(sorted(str(2*n))) ==  ''.join(sorted(str(3*n))) == ''.join(sorted(str(4*n))) == ''.join(sorted(str(5*n))) == ''.join(sorted(str(6*n))):
        return n

n = 1
while same_digit(n)==None:
    n += 1
    
print('The smallest positive integer is %d:' %n)