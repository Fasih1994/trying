#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 10:15:50 2018

@author: fasih
"""

import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[3,5,2],[5,2,8],[3,6,9]])
print('A: \n',A,'\nB: \n',B)
print('\nAdditon of A & B: \n',A+B)
print('\nMultiplication of A & B: \n',A*B)
print('\nTranspose of A:\n',np.transpose(A))
print('\nDeterminent of B:\n',np.linalg.det(B))
print('\nInverse of B:\n',np.linalg.inv(B))
print('\nRank of B:',np.rank(A))
