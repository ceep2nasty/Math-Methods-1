# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 19:46:22 2025

@author: coled_agkeohi
"""

# MM1 HW3 P3

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1) Symbols and exact solution
# -----------------------------
x, t = sp.symbols('x t', real=True)
y_exact_sym = sp.exp(x**2/2)  # exact solution e^{x^2/2}

def picard_iteration(k):
    yk = sp.Integer(1)
    seq= [yk]
    
    for _ in range(k):
        integral = sp.integrate (t * yk.subs(x,t), (t, 0, x))
        yk = sp.simplify( 1 + integral)
        seq.append(yk)
        
    return seq

y0, y1, y2, y3, y4, y5 = picard_iteration(5)

y_exact = sp.lambdify(x, y_exact_sym, 'numpy')
y1_num = sp.lambdify(x, y1, 'numpy')
y3_num = sp.lambdify(x, y3, 'numpy')
y5_num = sp.lambdify(x, y5, 'numpy')

X = np.linspace(-4,4, 500)

plt.figure(figsize=(6,6))
