# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]

arr = np.array(my_data)

d = {'a': 10, 'b': 20, 'c': 30}

pd.Series(data = my_data, index=labels)

pd.Series(my_data, labels)

pd.Series(my_data)

pd.Series(d)

pd.Series(data = labels)

ser1 = pd.Series([1, 2, 3, 4], ['Singapore', 'USA', 'Germany', 'Russia'])

ser2 = pd.Series([1, 2, 5, 4], ['Singapore', 'USA', 'Japan', 'Russia'])

ser3 = pd.Series(data=labels)

ser3[0]

ser1 + ser2