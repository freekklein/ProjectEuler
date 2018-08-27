# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

fifth_power_dict = dict()
for i in range(0,10):
    fifth_power_dict[i] = i**5

temp2 = []
for i in range(10,1000000):
    i_str = str(i)
    temp = []
    for j in i_str:
        temp.append(fifth_power_dict[int(j)])
    if sum(temp) == i:
        print(i)
        temp2.append(i)
        
print('Sum of these numbers: %d' %sum(temp2))