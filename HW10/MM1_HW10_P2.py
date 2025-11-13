# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 20:41:42 2025

@author: coled_agkeohi
"""

#MM1 HW10 P2: Newton's method to find root

import numpy as np
import matplotlib.pyplot as plt

# from solve, we have

def k_nplus(k):
    return k - (np.tan(k)-2/k)/(np.cos(k)**-2 + (2/k**2))

# initialize k as pi/4, the middle of our identified bracket

k = np.pi/4.0 

# initialize residual and tolerance

k_res = abs(k-k_nplus(k))
tol = 1e-5

# while loop to iterate through

while k_res > tol:
    k_new = k_nplus(k)   # store a k_new value
    k_res = abs(k-k_new) # check how close it is to tol
    k = k_new            # update and check again
    
    
# huzzah we have solved it. lets plot the solution 

x = np.linspace(0, 4*np.pi, 1000)
y = np.cos(x)

plt.plot(x, y)
plt.title(f'y(x) = cos({k_new:.4f}x)')
plt.xlabel('x')
plt.ylabel('y(x)')
    
    