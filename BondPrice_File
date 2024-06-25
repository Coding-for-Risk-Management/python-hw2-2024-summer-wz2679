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
