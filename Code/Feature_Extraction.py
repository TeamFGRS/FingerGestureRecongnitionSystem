import pandas as pd

import numpy as np

import seaborn as sns

from statsmodels.tsa.stattools import acovf

from Sensor_Data_Reader import *

#finger up file
fingerUp=read_file('../DataSet/Finger_up.csv')

#finger down
fingerDown=read_file('../DataSet/Finger_down.csv')

#finger left
fingerLeft=read_file('../DataSet/Finger_Left.csv')

#finger right
fingerRight=read_file('../DataSet/Finger_right.csv')

#90 deg clock
fingerClock=read_file('../DataSet/90deg_clockwise.csv')

#90 deg counter
fingerCounter=read_file('../DataSet/90deg_counter_clockwise.csv')


pd.to_csv('../DataSet/Feature_Extracted_Data.csv')
read_file(d_file)[‘A’].mean()

data[‘A’].var()

data[‘A’].skew()

sns.distplot(data[‘A’],hist=True,kde=True)

statsmodels.tsa.stattools.acovf(x, adjusted=False, demean=True, fft=True, missing='none', nlag=None)
#where x is the time series data.

"""
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import acovf


def extract_features(df, autocovar_num, dft_amplitudes_num):
    features = pd.DataFrame(columns=df.columns, dtype=np.float64)

    def add_2_features(index, df):
        def order_by_column(series):
            return series[features.columns].values

        features.loc[index, :] = order_by_column(df)

    # TODO: DRY with add_dft_amplitudes_of_df_2_features
    def add_autocovariance_of_df_2_features():
        def autocovariance_of_df(lag):
            return df.apply(lambda col: acovf(col)[lag], axis='index')

        for lag in range(1, autocovar_num + 1):
            add_2_features('autocovar_lag_' + str(lag), autocovariance_of_df(lag=lag))

    def add_dft_amplitudes_of_df_2_features():
        def dft_amplitudes_of_df(num):
            # FIXME: FFT ist hier falsch eingesetzt, da SVC schlechter geworden ist.
            return df.apply(lambda col: np.abs(np.fft.fft(col))[num], axis='index')

        for num in range(1, dft_amplitudes_num + 1):
            add_2_features('dft_amplitude_' + str(num), dft_amplitudes_of_df(num - 1))

    add_2_features('min', df.min())
    add_2_features('max', df.max())
    add_2_features('mean', df.mean())
    add_2_features('var', df.var(ddof=0))
    add_2_features('skew', df.skew())
    add_2_features('kurtosis', df.kurtosis())
    add_autocovariance_of_df_2_features()
    add_dft_amplitudes_of_df_2_features()
    return features
"""