import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import re
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_csv('C://Users//wyzdw//Desktop//data2.csv', index_col=['类型', 'ID', '日期'])
data = data.drop_duplicates()
