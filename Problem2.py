# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

i = 1
j = 2
temp =[]
temp.append(i)
temp.append(j)

while i+j<4*1e+06: 
    k = i+j
    temp.append(k)
    i = j
    j = k

print(sum(temp))