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
