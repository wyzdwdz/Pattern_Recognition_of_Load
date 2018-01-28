import re
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

def fillnull(array):
    array = np.where(array > 0, array, np.nan)

    mean = np.nanmean(array, axis=0)

    array_null = np.isnan(array)
    x_list, y_list = np.where(array_null)

    df_array = DataFrame(array)
    array_temp = df_array.fillna(df_array.mean())
    array_temp = array_temp.T

    Weights = 1. / 3.

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        if mean[y] == np.nan:
            continue
        elif y_list[i] in [0, 1, 94, 95]:
            array[x][y] = array_temp[x][y]
        elif x_list[i] in [0, array.shape[0]-1]:
            array[x][y] = array_temp[x][y]
        elif np.nan in [array_temp[x + 1][y], array_temp[x - 1][y], array_temp[x][y + 1], array_temp[x][y - 1]]:
            array[x][y] = array_temp[x][y]
        else:
            array[x][y] = 0.5 * (Weights * (array_temp[x + 1][y] + array_temp[x - 1][y]) + Weights * (array_temp[x][y + 1] + array_temp[x][y - 1])) + Weights * array_temp[x][y]

    sigma = np.std(array, axis=0)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        if mean[y] == np.nan:
            continue
        elif np.abs(array[x][y] - mean[y]) > (3 * sigma[y]):
            array_new = 0.2 * (array_temp[x][y+2] + array_temp[x][y-2] + array_temp[x][y+1] + array_temp[x][y-1] + array_temp[x][y])
            sigma_new = np.abs(array_temp[x][y] - array_new)
            if sigma_new >= 0.1 * array_new:
                array[x][y] = 0.5 * (array_new + array[x][y])
            else:
                array[x][y] = 0.5 * (0.375 * (array_temp[x][y+1] + array_temp[x][y-1]) + 0.125 * (array_temp[x][y+2] + array_temp[x][y-2])) + 0.5 * array_temp[x][y]

    return array


data = pd.read_csv('C://Users//wyzdw//Desktop//data_within_null.csv', index_col=['类型', 'ID', '日期'])

b_list = []
for a, b, c in list(data.index.values):
    if b in b_list:
        continue
    else:
        b_list.append(b)

data_ndarray = np.array([])

for id in b_list:
    array = data.loc(axis=0)[:, id].values
    if True not in np.isnan(array):
        if data_ndarray.size is 0:
            data_ndarray = array
        else:
            data_ndarray = np.concatenate((data_ndarray, array), axis=0)
    else:
        if data_ndarray.size is 0:
            data_ndarray = fillnull(array)
        else:
            data_ndarray = np.concatenate((data_ndarray, fillnull(array)), axis=0)

data_new = DataFrame(data_ndarray, index = data.index, columns = data.columns)
