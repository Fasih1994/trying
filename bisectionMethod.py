#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 10:16:32 2018

@author: fasih
"""
def bisect(a,b,iterr):
    x = (a+b)/2
    iterr+=1
    print("Iteration",iterr,"x=",x)
    return x,iterr    
def f(x):
    y = x**3-4*x-9
    return y

iterr = 0
a = int(input("Enter Value of a:"))
b = int(input("Enter Value of b:"))
aerr = float(input("Enter the allowed Error:"))
maxiter = int(input('Enter maximum iteration:'))
x,iterr = bisect(a,b,iterr) 
while iterr<maxiter:
    if f(a)*f(x)<0:
        b=x
    else:
        a=x
    x1,iterr = bisect(a,b,iterr)
    if abs(x1-x)<aerr:
        print("After",iterr,"iterations, root =",x1 )
        break
    x=x1
if iterr ==maxiter:
    print("iteration cannot be obtained!")
    


