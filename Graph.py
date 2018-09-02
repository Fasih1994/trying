#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:07:33 2018

@author: fasih
"""

# graph of sin(x) from -pi t0 pi

import numpy as np 
import matplotlib.pyplot as plt

print("Graph of Question 1:")
# Assigning values
x = np.linspace( -np.pi, np.pi)
y = np.sin(x)

# Plotting graph
plt.title('Graph of Sin(x) from -Pi to Pi')
plt.xlabel('Value of from -Pi to Pi as x')
plt.ylabel( 'Function of Sin(x)')
plt.plot(x,y,'-.')
plt.show()


print("Graph of Question 2:")
# Assigning values
x = np.linspace( -2, 2)
y = np.exp(x)-x-2

# Plotting graph
plt.title('Graph of e^x-x-2 from -2 to 2')
plt.xlabel('Value of from -2 to 2 as x')
plt.ylabel( 'Function of e^x-x-2')
plt.plot(x,y,'-o')
plt.show()