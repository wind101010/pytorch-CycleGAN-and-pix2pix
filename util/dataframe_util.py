
import numpy as np
from PIL import Image
import pandas as pd

import os

#

def join_dataframe_list(dataframe_list_a,dataframe_list_b):
    count =  len(dataframe_list_a) if len(dataframe_list_a)>len(dataframe_list_b) else len(dataframe_list_b)
    result_df_list = list()
    for i in range(0,count):
        ope_df_a = dataframe_list_a[i]
        ope_df_b = dataframe_list_b[i]
        print(ope_df_a,ope_df_b)
        resultdf = pd.concat([ope_df_a,ope_df_b],join='outer',axis=1)

        result_df_list.append(resultdf)
    return result_df_list
