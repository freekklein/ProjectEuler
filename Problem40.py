# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 23:14:30 2018

@author: Freek
"""

temp = []
for i in range(0,500000):
    temp += str(i)
    
temp2 = ''.join(temp)
print('Value is %d' %(int(temp2[1])*int(temp2[10])*int(temp2[100])*int(temp2[1000])*
                      int(temp2[10000])*int(temp2[100000])*int(temp2[1000000])))