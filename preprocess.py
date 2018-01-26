import re
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

data = data.drop(['户名', '户号', '地址', '工程期数'], axis=1)      #删除dataframe列

regex = re.compile('[0-9]')
data['地址码'] = data['地址码'].replace(regex, '')         #将"地址码"中元素的数字删除

data = data.sort_values(by=['ID', '日期'])           
data['日期'] = pd.to_datetime(data['日期'], format='%Y-%m-%d %H:%M:%S')     #将日期改为datetime格式
data.rename(columns={'地址码':'类型'}, inplace=True)

columns = data.columns.tolist()
i = columns.index('ID')
j = columns.index('类型')
columns[i], columns[j] = columns[j], columns[i]
data = data[columns]                                       #将'ID'、'类型'调换位置

data = data.sort_values(by=['类型', 'ID', '日期'])
data = data.set_index(['类型', 'ID', '日期'])
