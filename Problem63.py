# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
counter = 0
for i in range(1,10):
    for j in range(1,10):
        if i == len(str(pow(i,j))):
            #print(i, pow(i,j))
            counter += 1
            
print(counter)