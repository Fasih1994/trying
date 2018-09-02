#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 02:07:33 2018

@author: fasih
"""

import re

run = True
previous = 0

def performMath():
    global previous
    global run
    equation = ''
    equation = input("Enter an Eqaution:")
#    if previous == 0:
#        equation = input("Enter an Eqaution:")
#    else:
#        equation = input(str(previous))
        
    if equation == 'quit':
        print("GoodBay Human!")
        run = False
    else:
        previous = eval(equation)
        equation = re.sub('[A-Za-z,.:()" "]','',equation)
#        if previous == 0:
#            previous = eval(equation)
#        else:
#            previous = eval(str(previous) + equation)
        print(previous)
        
while run:
    performMath()