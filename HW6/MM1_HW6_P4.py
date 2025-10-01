# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 15:38:07 2025

@author: coled_agkeohi
"""

# MM1 HW6 P4

import numpy as np
import matplotlib.pyplot as plt

def y_of_x (x, eps):
    c = np.sqrt(2) * (x**2 + 1)**(-0.5)
    c2 = np.sinh((x+(x**3)/3)/eps)/np.sinh(4/(3*eps))
    return c*c2

x = np.linspace(0, 1, 100)
eps = 0.1
y = np.zeros_like(x)

for i in range(len(x)):
    y[i] = y_of_x(x[i], 0.1)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("WKBJ with eps = 0.1")

