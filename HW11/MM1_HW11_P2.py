# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 19:08:29 2025

@author: coled_agkeohi
"""

# MM1 HW11

import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(0,1, 100)

def y_x(x):
    return 6*x - 6*x**2

yy = y_x(xx)

plt.plot(xx, yy)
plt.title('Extremizing function of integral')
plt.xlabel('x')
plt.ylabel('y(x)')