# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:07:36 2021

@author: Donat
"""

phrase = "python test"
print(phrase.replace("test", "fest").upper().isupper())

from math import *

number = 4.7
print(floor(number))
print(ceil(number))

def mathing():
    m1 = input("Enter a number: ")
    m2 = input("Enter another number: ")
    result = float(m1)+float(m2)
    print(result)
    
# mathing()

dogs = ["Bodri", "Foltos", "Koromos", "Vilmos"] #lists
nums = [2, 6, 8, 33, 24, 56, 5]
nums2 = [[3, 6], [3, 6]]
nums.sort()
print(dogs[2:])
print(nums)
print (nums2[1])
nums2[1] = 5
print(nums2)

tuplenums = (2, 6, 8, 33, 24, 56, 5) #tuple, so you cant change

monthConversions = {
    "Jan": "January",
    "Feb": "February"
}

print(monthConversions["Feb"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Bla"))

list2d = [
    [1, 4, 6, 6],
    [1, 4, 6],
    [1, 2, 6, 4, 45]
    ]

print(list2d[2][4])

for row in list2d:
    for col in row:
        print(col)


try:
    value = 10/2
    print(value)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)




