import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'],['W', 'X', 'Y', 'Z'])

df['W']

df

df.W

df[['W', 'Z']]

df['new'] = df['W'] + df['Y']

df.drop('new', axis=1, inplace=True) 

df.drop('E', axis=0)

df.loc['A']

df.iloc[0]

df.loc[['A', 'B'], ['W', 'Y']]


# Dataset part 2
booldf = df > 0

df[df > 0]

df['W'] > 0

df[df['W'] > 0]

df[df['W'] > 0][['Y', 'X']]
 
df[(df['W']> 0) & (df['Y'] > 1)]

index = df.reset_index()

new_index = 'CA NY WY OR '.split()

df['States'] = new_index

df.set_index('States')

test_df = df

test_df['W'].shape