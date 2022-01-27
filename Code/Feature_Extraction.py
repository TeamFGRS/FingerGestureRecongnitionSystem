import csv

import pandas as pd
import numpy as np
import seaborn as sns

from statsmodels.tsa.stattools import acovf


def feature_extraction(data_file, test_type, ring_number):
    # TODO:min, max, mean skewness, kurtosis, variance, autocovariance(?)

    # for TEST in data_file['TEST'].unique():
    #     locals()['data_file_' + TEST] = data_file[(data_file.TEST == TEST)]
    #     print(locals()['data_file_' + TEST])

    features = pd.DataFrame(data_file)
    grouped = features.groupby(features["TEST"])

    # test_column = grouped.head()
    # print("Start Test")
    # print(grouped.get_group("5"))
    # print("End Test")

    # feature_file = open('../DataSet/extracted_features.csv', 'w')
    # writer = csv.writer(feature_file)


    for group in range(grouped.ngroups - 1):
        df = grouped.get_group(str(group + 1)).drop(columns="TEST")
        kurt = df.kurt().to_frame().transpose()



        # kurt_values = kurt.iloc[0:, :]
        # header = ["ACC-X", "ACC-Y", "ACC-Z", "GYRO-X", "GYRO-Y", "GYRO-Z"]
        #kurt.DictWriter()
        kurt.to_csv('../DataSet/extracted_features.csv', mode='a', index=False, header=False)
        #file_test.to_csv('../DataSet/extracted_features_trial.csv',mode='a', header=["ACC-X", "ACC-Y", "ACC-Z", "GYRO-X", "GYRO-Y", "GYRO-Z"], index=False)

        # print(kurt)
        # writer.writerow([kurt])

        # print(df.kurtosis())

    # feature_file.close()

    return 1

    # grouped = data_file.groupby(data_file.TEST)
    # print(grouped.ngroups)
    # df5 = grouped.get_group("2000")
    # print(df5)

    # for value in test_num:
    #     if str(value) == str(test_num):
    #         separate_test_instances = pd.DataFrame(columns=data_file.columns, dtype=np.float64)
    #         print(separate_test_instances)

    # #create data structure
    # features = pd.DataFrame(columns=data_file.columns, dtype=np.float64)
    #
    # def append_features(label, data_file):
    #     def ordering(col_values):
    #         return col_values[features.columns].values
    #
    #     #check label and store associated values
    #     features.loc[label, :] = ordering(data_file)
    #
    # append_features('min', data_file.min())
    # append_features('max', data_file.max())
    # append_features('mean', data_file.mean())
    # append_features('var', data_file.var(ddof=0))
    # append_features('skew', data_file.skew())
    # append_features('kurtosis', data_file.kurtosis())
    #
    # return features
