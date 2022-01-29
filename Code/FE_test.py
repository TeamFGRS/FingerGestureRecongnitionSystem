import pandas as pd
import numpy as np
import seaborn as sns

from statsmodels.tsa.stattools import acovf


def fe_test(data_file, test_type, ring_number):
    gesture_df = pd.DataFrame(data_file)
    grouped = gesture_df.groupby(gesture_df["TEST"])

    # print(grouped.get_group(1))
    i=0
    for group in gesture_df['TEST'].unique():
        print(group)
        i=i+1

    print("LENGTH:  ", len(grouped.groups.keys()), grouped.ngroups, i)
    # print(grouped.get_group("1"))
    # for group in range(grouped.ngroups):
    #     print(grouped.get_group(group+1))
    # for group in grouped:
    #     group
    return 1
