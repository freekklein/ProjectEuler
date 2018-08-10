# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

i=1
temp_3 = []
while 3*i<1000:
    temp_3.append(3*i)
    i += 1

i=1
temp_5 = []
while 5*i<1000:
    temp_5.append(5*i)
    i+=1
    
print(sum(temp_3+temp_5))