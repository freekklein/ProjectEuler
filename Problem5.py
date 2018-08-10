# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:13:50 2018

@author: EL11LV
"""

number = 2520
while len([i for i in range(1,21) if number % i]) > 0:
    number += 1
print('Smallest positive number: %d' %number)