#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:25:01 2018

@author: fasih
"""
import numpy as np
def f(x):
    y = (np.cos(x))-(x*(np.exp(x)))
    return y

def regulaFalsi(x0,x1,iterr):
    x = x0 - ((x1-x0)/(f(x1)-f(x0)))*f(x0)
    iterr+=1
    print('At',iterr,'iteration . Root:',x)
    return x,iterr



x0 = int(input('Enter x0:'))
x1 = int(input('Enter x1:'))
max_iter = int(input('Enter Max Iterations:'))
err = float(input('Enter acceptable error value:'))
iterr=0

x,iterr = regulaFalsi(x0,x1,iterr)
while iterr<max_iter:
    if f(x)*f(x0) < 0:
        x0 = x
    else:
        x1 = x
    x3,iterr = regulaFalsi(x0,x1,iterr)
    if abs(x3-x) < err:
        print('\n===========================================')
        print('After',iterr,'iterations. Root:',x3)
        break
    x=x3
if iterr == max_iter:
    print('Result not found.\nTry again with more iterations.')