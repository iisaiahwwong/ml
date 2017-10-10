# Multiple Linear Regression

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Categorical Encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder_x = LabelEncoder()
X[:, 3] = label_encoder_x.fit_transform(X[:, 3])
onehot_encoder = OneHotEncoder(categorical_features=[3])
X = onehot_encoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building the optimal model using backward elimination
import statsmodels.formula.api as sm
# add arrays of ones to act as b0
X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:, [0, 3, 4, 5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:, [0, 3, 5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:, [0, 3]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()