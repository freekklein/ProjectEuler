# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 23:43:23 2018

@author: Freek
"""

S = []

for i in range(1,101):
    S.append(i**2)
    
from itertools import combinations

#S = [1,3,6,8,10,11]
S_subset = list(combinations(S,50))

temp = []
for i in S_subset:
    temp.append(sum(i))
    
import pandas as pd
    
temp = pd.value_counts(pd.Series(temp))[pd.value_counts(pd.Series(temp))==1].index
    
print(sum(temp))