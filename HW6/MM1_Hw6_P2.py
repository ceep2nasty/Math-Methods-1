# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 21:08:10 2025

@author: coled_agkeohi
"""

import sympy as sp

x, eps = sp.symbols('x eps', positive = True)
y = sp.Function('y')

ode = sp.Eq(eps*sp.diff(y(x), x, 2) - sp.diff(y(x), x), 1)

y_general = sp.dsolve(ode)

ics = {y(0):0, y(1): 0}

y_exact = sp.dsolve(ode, ics =ics)



import numpy as np
import matplotlib.pyplot as plt

# Exact solution as a lambda
y_exact_func = sp.lambdify((x, eps), y_exact.rhs, 'numpy')

# Composite approximation
def y_approx(x, eps):
    return -x + np.exp((x-1)/eps)

# Set eps value
eps_val = 0.1
x_vals = np.linspace(0, 1, 400)
y_exact_vals = y_exact_func(x_vals, eps_val)
y_approx_vals = y_approx(x_vals, eps_val)

# Plot
plt.figure(figsize=(7,5))
plt.plot(x_vals, y_exact_vals, label="Exact", linewidth=2)
plt.plot(x_vals, y_approx_vals, '--', label="Approx (composite)")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.title(f"Comparison for ε={eps_val}")
plt.grid(True)
plt.show()
