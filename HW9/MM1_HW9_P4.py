# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 12:00:55 2025

@author: coled_agkeohi
"""

#MM1 HW9 P3

# Find the smallest root of tan(k) - (2/k) = 0

import numpy as np
import matplotlib.pyplot as plt


def f(k):
    return np.tan(k) - 2.0/k

def bisect(f, a, b, maxit=100, tol=1e-12):
    fa, fb = f(a), f(b)
    if np.sign(fa) * np.sign(fb) >= 0:
        raise ValueError("Interval does not bracket a root")
    for _ in range(maxit):
        c = 0.5*(a+b)
        fc = f(c)
        if abs(fc) < tol or 0.5*(b-a) < tol:
            return c
        if np.sign(fa) * np.sign(fc) < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return 0.5*(a+b)

# Smallest root is in (0, pi/2); avoid endpoints by epsilon
eps = 1e-8
k1 = bisect(f, eps, 0.5*np.pi - eps)
print(k1)  # 1.0768739863122552

# plot it 

k = 1.076873986
x = np.linspace(0,1,400)
y = np.cos(k*x)             # A=1
plt.plot(x,y); plt.xlabel('x'); plt.ylabel('y(x)'); plt.show()


        
    
    
    


