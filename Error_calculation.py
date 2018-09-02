#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:28:52 2018

@author: fasih
"""

import numpy as np

pi = 22/7
piDecimal = np.pi
abslError = abs(piDecimal-pi)
reltError = abslError/piDecimal
percError = reltError*100

print("pi =",piDecimal)
print('22/7 =',pi)
print('\nAbolute Error:',abslError)
print('\nRelative Error:',reltError)
print('\nPercentage Error:',percError)