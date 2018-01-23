import re
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

data = data.drop(['户名', '户号', '地址', '工程期数'])

regex = re.compile('[1-9]')
data['地址码'] = data['地址码'].replace(regex, '')

data2 = DataFrame()
data2 = data.sort_values(by=['ID', '日期'])
data2['日期'] = pd.to_datetime(data2['日期'], format='%Y-%m-%d %H:%M:%S')
data2.rename(columns={'地址码':'类型'}, inplace=True)
columns = data2.columns.tolist()

i = columns.index('ID')
j = columns.index('类型')
columns[i], columns[j] = columns[j], columns[i]
data2 = data2[columns]

data3 = DataFrame()
data3 = data2.sort_values(by=['类型', 'ID', '日期'])
data4 = data3.set_index(['类型', 'ID', '日期'])
