# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:04:05 2024

@author: Lenovo
"""

def WhoAmI():
    return('wz2679')

result = WhoAmI()
print(result)

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy

    C = face * couponRate / ppy

    discount_factors = (1 + y / ppy) ** np.arange(1, n + 1)

    pv_coupons = C / discount_factors

    pv_face = face / discount_factors[-1]

    bond_price = np.sum(pv_coupons) + pv_face
    
    return bond_price

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10

price = getBondPrice(y, face, couponRate, m)
print(price)




import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy

    C = face * couponRate / ppy

    discount_factors = (1 + y / ppy) ** np.arange(1, n + 1)

    pv_coupons = C / discount_factors

    pv_face = face / discount_factors[-1]

    weighted_time = np.arange(1, n + 1) * pv_coupons
    weighted_time = np.sum(weighted_time)+ n * pv_face  
    total_present_value = np.sum(pv_coupons) + pv_face
    macaulay_duration =  weighted_time/ total_present_value
    
    return macaulay_duration

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

# Calculate bond duration
duration = getBondDuration(y, face, couponRate, m, ppy)
print(duration)


import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)
    
    # Conditions for FizzBuzz
    condlist = [
        (numbers % 15 == 0),
        (numbers % 3 == 0),
        (numbers % 5 == 0)
    ]
    
    choicelist = ['FizzBuzz', 'Fizz', 'Buzz']
    
    output = np.select(condlist, choicelist, default=numbers.astype(str))
    
    # Convert numpy array to Python list
    return output.tolist()

# Test
start = 1
finish = 15
result = FizzBuzz(start, finish)
print(result)
