# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 20:25:49 2025

@author: coled_agkeohi
"""
import numpy as np
import matplotlib.pyplot as plt

# MM1 Homework 6 Problem 1

def y_solns(x, epsilon):
    y0 = x
    y1 = y0 + epsilon* ((x-x**4)/12)
    y2 = y1 + (epsilon**2)* ( (1/252)*x**7 - (1/72) * x **4 + (5/504) * x)
    return y0, y1, y2

x = np.linspace(0, 2, 100)
eps1 = 0.25
eps2 = 0.1
y0e1, y1e1, y2e1, y0e2, y1e2, y2e2 = (np.zeros_like(x) for _ in range(6))
for i in range(len(x)):
    y0e1[i], y1e1[i], y2e1[i] = y_solns(x[i], eps1)
    y0e2[i], y1e2[i], y2e2[i] = y_solns(x[i], eps2)
    
    
fig1, ax1 = plt.subplots()

ax1.plot(x, y0e1, label='y0')
ax1.plot(x, y1e1, label='y1')
ax1.plot(x, y2e1, label='y2')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Solutions y0, y1, y2 with epsilon = 0.25')

ax1.legend() 


fig2, ax2 = plt.subplots()

ax2.plot(x, y0e2, label='y0')
ax2.plot(x, y1e2, label='y1')
ax2.plot(x, y2e2, label='y2')

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Solutions y0, y1, y2 with epsilon = 0.1')

ax2.legend()


plt.show()
