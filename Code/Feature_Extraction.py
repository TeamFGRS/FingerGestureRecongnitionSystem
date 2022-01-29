import csv

import pandas as pd
import numpy as np
import seaborn as sns

from statsmodels.tsa.stattools import acovf


def feature_extraction(data_file, test_type, ring_number):
    # TODO:min, max, mean skewness, kurtosis, variance, autocovariance(?)

    features = pd.DataFrame(data_file)
    grouped = features.groupby(features["TEST"])

    # gesture_df = pd.DataFrame()
    # def test_type():
    #     test = pd.DataFrame()
    #
    #     return test
        # for group in range(grouped.ngroups - 1):
        #     test = test.

    def minimum(data_group):
        min_df = data_group.min().to_frame().transpose()
        min_df_2 = min_df.reset_index(drop=True)
        min_df_3 = min_df_2.set_axis(
            ['ACC-X-MIN-' + str(ring_number), 'ACC-Y-MIN-' + str(ring_number), 'ACC-Z-MIN-' + str(ring_number),
             'GYRO-X-MIN-' + str(ring_number), 'GYRO-Y-MIN-' + str(ring_number), 'GYRO-Z-MIN-' + str(ring_number)],
            axis=1, inplace=False)
        return min_df_3

    def min_df():
        min_df = minimum(grouped.get_group(1).drop(columns="TEST"))
        # print(min_df)
        for group in range(grouped.ngroups - 1):
            min_df = min_df.append(minimum(grouped.get_group(group + 2).drop(columns="TEST")), ignore_index=True)
        return min_df

    def maximum(data_group):
        max_df = data_group.max().to_frame().transpose()
        max_df_2 = max_df.reset_index(drop=True)
        max_df_3 = max_df_2.set_axis(
            ['ACC-X-MAX-' + str(ring_number), 'ACC-Y-MAX-' + str(ring_number), 'ACC-Z-MAX-' + str(ring_number),
             'GYRO-X-MAX-' + str(ring_number), 'GYRO-Y-MAX-' + str(ring_number), 'GYRO-Z-MAX-' + str(ring_number)],
            axis=1, inplace=False)
        return max_df_3

    def max_df():
        max_df = maximum(grouped.get_group(1).drop(columns="TEST"))
        # print(min_df)
        for group in range(grouped.ngroups - 1):
            max_df = max_df.append(maximum(grouped.get_group(group + 2).drop(columns="TEST")), ignore_index=True)
            # max_df = pd.concat()
        return max_df

    def mean(data_group):
        mean_df = data_group.mean().to_frame().transpose()
        mean_df_2 = mean_df.reset_index(drop=True)
        mean_df_3 = mean_df_2.set_axis(
            ['ACC-X-MEAN-' + str(ring_number), 'ACC-Y-MEAN-' + str(ring_number), 'ACC-Z-MEAN-' + str(ring_number),
             'GYRO-X-MEAN-' + str(ring_number), 'GYRO-Y-MEAN-' + str(ring_number), 'GYRO-Z-MEAN-' + str(ring_number)],
            axis=1, inplace=False)
        return mean_df_3

    def mean_df():
        mean_df = mean(grouped.get_group(1).drop(columns="TEST"))
        # print(min_df)
        for group in range(grouped.ngroups - 1):
            mean_df = mean_df.append(mean(grouped.get_group(group + 2).drop(columns="TEST")), ignore_index=True)
            # max_df = pd.concat()
        return mean_df

    def variance(data_group):
        var_df = data_group.var(ddof=0).to_frame().transpose()
        var_df_2 = var_df.reset_index(drop=True)
        var_df_3 = var_df_2.set_axis(
            ['ACC-X-VAR-' + str(ring_number), 'ACC-Y-VAR-' + str(ring_number), 'ACC-Z-VAR-' + str(ring_number),
             'GYRO-X-VAR-' + str(ring_number), 'GYRO-Y-VAR-' + str(ring_number), 'GYRO-Z-VAR-' + str(ring_number)],
            axis=1, inplace=False)
        return var_df_3

    def variance_df():
        var_df = variance(grouped.get_group(1).drop(columns="TEST"))
        # print(min_df)
        for group in range(grouped.ngroups - 1):
            var_df = var_df.append(variance(grouped.get_group(group + 2).drop(columns="TEST")), ignore_index=True)
            # max_df = pd.concat()
        return var_df

    def skewness(data_group):
        skew_df = data_group.skew().to_frame().transpose()
        skew_df_2 = skew_df.reset_index(drop=True)
        skew_df_3 = skew_df_2.set_axis(
            ['ACC-X-SKEW-' + str(ring_number), 'ACC-Y-SKEW-' + str(ring_number), 'ACC-Z-SKEW-' + str(ring_number),
             'GYRO-X-SKEW-' + str(ring_number), 'GYRO-Y-SKEW-' + str(ring_number), 'GYRO-Z-SKEW-' + str(ring_number)],
            axis=1, inplace=False)
        return skew_df_3

    def skewness_df():
        skew_df = skewness(grouped.get_group(1).drop(columns="TEST"))
        # print(min_df)
        for group in range(grouped.ngroups - 1):
            skew_df = skew_df.append(skewness(grouped.get_group(group + 2).drop(columns="TEST")), ignore_index=True)
            # max_df = pd.concat()
        return skew_df

    def kurtosis(data_group):
        kurt_df = data_group.kurtosis().to_frame().transpose()
        kurt_df_2 = kurt_df.reset_index(drop=True)
        kurt_df_3 = kurt_df_2.set_axis(
            ['ACC-X-KURT-' + str(ring_number), 'ACC-Y-KURT-' + str(ring_number), 'ACC-Z-KURT-' + str(ring_number),
             'GYRO-X-KURT-' + str(ring_number), 'GYRO-Y-KURT-' + str(ring_number), 'GYRO-Z-KURT-' + str(ring_number)],
            axis=1, inplace=False)
        return kurt_df_3

    def kurtosis_df():
        kurt_df = kurtosis(grouped.get_group(1).drop(columns="TEST"))
        # print(min_df)
        for group in range(grouped.ngroups - 1):
            kurt_df = kurt_df.append(kurtosis(grouped.get_group(group + 2).drop(columns="TEST")), ignore_index=True)
            # max_df = pd.concat()
        return kurt_df

    # print(min_df())
    # print(max_df())
    c_df = min_df().join(max_df()).join(mean_df()).join(variance_df()).join(skewness_df()).join(kurtosis_df())
    c_df.insert(0, 'GESTURE', test_type)
    # print(c_df)
    # print(test_type())
    # c_df.to_csv('../DataSet/extracted_features.csv', mode='a', index=False)

    # for group in range(grouped.ngroups - 1):
    #     df = grouped.get_group(str(group + 1)).drop(columns="TEST")
    #     print(minimum(df))

    # kurt.to_csv('../DataSet/extracted_features.csv', mode='a', index=False, header=False)

    return c_df

    # file_test.to_csv('../DataSet/extracted_features_trial.csv',mode='a', header=["ACC-X", "ACC-Y", "ACC-Z", "GYRO-X", "GYRO-Y", "GYRO-Z"], index=False)

    # print(kurt)
    # writer.writerow([kurt])

    # print(df.kurtosis())

    # feature_file.close()

    # kurt_values = kurt.iloc[0:, :]
    # header = ["ACC-X", "ACC-Y", "ACC-Z", "GYRO-X", "GYRO-Y", "GYRO-Z"]
    # kurt.DictWriter()

    # test_column = grouped.head()
    # print("Start Test")
    # print(grouped.get_group("5"))
    # print("End Test")

    # feature_file = open('../DataSet/extracted_features.csv', 'w')
    # writer = csv.writer(feature_file)



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
