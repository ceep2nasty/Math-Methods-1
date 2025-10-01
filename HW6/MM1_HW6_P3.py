# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 15:26:48 2025

@author: coled_agkeohi
"""

# MM1 HW6 Problem 3


import numpy as np
import matplotlib.pyplot as plt

# set up function for solution equation

def pendulum(x, eps):
    c1 = np.cos((1 + (1/16)*eps)*x) + ((eps**2) / 192) * (np.cos((1 + (1/16)*eps)*x)-np.cos((3+(3*eps)/16)*x))
    return eps * c1

x = np.linspace(0, 1, 100)
eps = 0.1
y = np.zeros_like(x)

for i in range(len(x)):
    y[i] = pendulum(x[i], 0.1)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_title("strained time solution with eps = 0.1")

