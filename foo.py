# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 06:39:31 2023

@author: Karl.Munroe
"""

def is_divisible_by_k(x, k):
 '''
 Checks whether x is divisible by k.
 '''
 # return assert (x%k == 0)
 # assertion not needed as both numbers are already integers
 if (x%k == 0):
     return True
 else:
     return False
'''
# end function 

Store all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
'''
x = [] # create a blank list
for i in range(1,1001,1): #KM - Use the range from 1 to 1000, 1001 is not included       
 if (is_divisible_by_k(i, 2) | is_divisible_by_k(i, 5)) |is_divisible_by_k(i, 7):
     x.append(i)

'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
# KM - Question: Are not numbers that are divisible by 2 doubles?
'''
print("The total list of elements found is: ")
print(x)
totalSum = sum(x)
print("The total of all elements is: %2d" % totalSum)

