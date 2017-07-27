import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'],['W', 'X', 'Y', 'Z'])

df['W']

df.W

df[['W', 'Z']]

df['new'] = df['W'] + df['Y']

df.drop('new', axis=1, inplace=True) 

df.drop('E', axis=0)

df.loc['A']

df.iloc[0]

df.loc[['A', 'B'], ['W', 'Y']]

df
