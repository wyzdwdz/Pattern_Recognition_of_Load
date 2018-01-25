import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import re
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_csv('C://Users//wyzdw//Desktop//data2.csv', index_col=['类型', 'ID', '日期'])
data = data.drop_duplicates()
np.size(np.where(np.isnan(data)))
data.index.is_lexsorted()
data.loc(axis=0)[:, 'H00011']

b_list = []
for a, b, c in list(data.index.values):
    if b in b_list:
        continue
    else:
        b_list.append(b)
        
data = data.fillna(method = 'bfill')
