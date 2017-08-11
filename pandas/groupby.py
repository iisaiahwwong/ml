import pandas as pd
import numpy as np

data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['San', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
        }

df = pd.DataFrame(data)

by_comp = df.groupby('Company')

by_comp.mean()
by_comp.sum()
by_comp.std()

by_comp.sum().loc['FB']

df.groupby('Person').sum()

df.groupby('Company').count()

df.groupby('Company').max()

df.groupby('Company').describe()