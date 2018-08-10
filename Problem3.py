# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

temp = []
number = 600851475143

for i in range(2,100000):
    if number % i == 0:
        print('Factor: %d' %i)
        temp2 = []
        for j in range(2,i):
            if i % j == 0:
                temp2.append(j)
        if len(temp2)==0:
            temp.append(i)
        else: break

print('Biggest Prime Factor for %d is: %d' %(number,max(temp)))