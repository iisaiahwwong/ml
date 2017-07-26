# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:15:40 2017

@author: intern
"""

import numpy as np

#Print Zero 
np.zeros(10)

#Print Ones
np.ones(10)

#Print fives
np.ones(10) * 5

# 10 to 50
np.arange(10, 51)

# 10 to 50 even
np.arange(10, 51, 2)

# 3x3
np.arange(9).reshape(3,3)

# identify matrix
np.eye(3)

#Gen a rand 0 and 1
np.random.rand(1)

#Gen 25 ran num
np.random.randn(25)

#gen range
np.linspace(0.01, 1, 100)

np.linspace(0, 1, 20)


mat = np.arange(1,26).reshape(5,5)

mat[2:,1:]

mat.sum(axis=0)
