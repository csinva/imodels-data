import numpy as np

import pandas as pd

# note: data from here https://github.com/shifwang/Enhancer/tree/master/data
# that repo also contains scripts for iRF results

X_train = pd.read_csv('../data/enhancer/01_X_train.csv', index_col=0)
X_test = pd.read_csv('../data/enhancer/02_X_test.csv', index_col=0)
y_train = pd.read_csv('../data/enhancer/03_y_train.csv', index_col=0).values.ravel()
y_test = pd.read_csv('../data/enhancer/04_y_test.csv', index_col=0).values.ravel()

df = pd.concat((X_train, X_test))
df['target'] = np.concatenate((y_train, y_test))
df.to_csv('../data_cleaned/enhancer.csv', index=False)
# print(df)
