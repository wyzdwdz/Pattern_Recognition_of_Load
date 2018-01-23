import re
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#生成一组{年份:文件路径}的字典year_str
#和一组{年份:[多个xls的Sheet名组成的list]}的字典month_str
years = list(range(2003, 2009))
months = list(range(1, 13))
year_str = {}
month_str = {}
for year in years:
    year_str[year] = 'C://Users//wyzdw//Desktop//dachuang//source//' + str(year) + '.xls'
    month_str[year] = []
    for month in months:
        month_str[year].append(str(year) + '-' + str(month))
for i in range(6):
    month_str[2008].pop()

#将所有文件和所有文件里的Sheets连接到一起组成DataFrame
data = DataFrame()
for year in year_str:
    with pd.ExcelFile(year_str[year]) as xls:
        for month_name in month_str[year]:
            data = data.append(pd.read_excel(xls, month_name), ignore_index=True)
