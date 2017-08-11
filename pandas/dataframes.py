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


# Dataframe part 2
booldf = df > 0

df[df > 0]

df['W'] > 0

df[df['W'] > 0]

df[df['W'] > 0][['Y', 'X']]
 
df[(df['W']> 0) & (df['Y'] > 1)]

index = df.reset_index()

new_index = 'CA NY WY OR '.split()
test_df = df

if len(new_index) != test_df['W'].shape:
    new_index.append('SG')

test_df['States'] = new_index

df['States'] = new_index

df.set_index('States')

test_df['W'].shape

#Dataframe part 3

outside = "G1 G1 G1 G2 G2 G2".split()
inside = list(map(int, "1 2 3 1 2 3".split()))
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])

df.loc['G1'].loc[1]

df.index.names = ['Groups', 'Num']
