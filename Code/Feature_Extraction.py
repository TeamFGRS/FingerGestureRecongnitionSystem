import pandas as pd


def feature_extraction(data_frame, test_type):
    # TODO: autocovariance(?), maybe fix warnings

    grouped = data_frame.groupby(data_frame["TEST"])

    def minimum(data_group):
        min_df = data_group.min().to_frame().transpose()
        min_df_2 = min_df.reset_index(drop=True)
        min_df_3 = min_df_2.set_axis(
            ['ACC-X-MIN-Ring1', 'ACC-Y-MIN-Ring1', 'ACC-Z-MIN-Ring1', 'GYRO-X-MIN-Ring1', 'GYRO-Y-MIN-Ring1',
             'GYRO-Z-MIN-Ring1', 'ACC-X-MIN-Ring2', 'ACC-Y-MIN-Ring2', 'ACC-Z-MIN-Ring2', 'GYRO-X-MIN-Ring2',
             'GYRO-Y-MIN-Ring2', 'GYRO-Z-MIN-Ring2'],
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
            ['ACC-X-MAX-Ring1', 'ACC-Y-MAX-Ring1', 'ACC-Z-MAX-Ring1', 'GYRO-X-MAX-Ring1', 'GYRO-Y-MAX-Ring1',
             'GYRO-Z-MAX-Ring1', 'ACC-X-MAX-Ring2', 'ACC-Y-MAX-Ring2', 'ACC-Z-MAX-Ring2', 'GYRO-X-MAX-Ring2',
             'GYRO-Y-MAX-Ring2', 'GYRO-Z-MAX-Ring2'],
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
            ['ACC-X-MEAN-Ring1', 'ACC-Y-MEAN-Ring1', 'ACC-Z-MEAN-Ring1', 'GYRO-X-MEAN-Ring1', 'GYRO-Y-MEAN-Ring1',
             'GYRO-Z-MEAN-Ring1', 'ACC-X-MEAN-Ring2', 'ACC-Y-MEAN-Ring2', 'ACC-Z-MEAN-Ring2', 'GYRO-X-MEAN-Ring2',
             'GYRO-Y-MEAN-Ring2', 'GYRO-Z-MEAN-Ring2'],
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
            ['ACC-X-VAR-Ring1', 'ACC-Y-VAR-Ring1', 'ACC-Z-VAR-Ring1', 'GYRO-X-VAR-Ring1', 'GYRO-Y-VAR-Ring1',
             'GYRO-Z-VAR-Ring1', 'ACC-X-VAR-Ring2', 'ACC-Y-VAR-Ring2', 'ACC-Z-VAR-Ring2', 'GYRO-X-VAR-Ring2',
             'GYRO-Y-VAR-Ring2', 'GYRO-Z-VAR-Ring2'],
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
            ['ACC-X-SKEW-Ring1', 'ACC-Y-SKEW-Ring1', 'ACC-Z-SKEW-Ring1', 'GYRO-X-SKEW-Ring1', 'GYRO-Y-SKEW-Ring1',
             'GYRO-Z-SKEW-Ring1', 'ACC-X-SKEW-Ring2', 'ACC-Y-SKEW-Ring2', 'ACC-Z-SKEW-Ring2', 'GYRO-X-SKEW-Ring2',
             'GYRO-Y-SKEW-Ring2', 'GYRO-Z-SKEW-Ring2'],
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
            ['ACC-X-KURT-Ring1', 'ACC-Y-KURT-Ring1', 'ACC-Z-KURT-Ring1', 'GYRO-X-KURT-Ring1', 'GYRO-Y-KURT-Ring1',
             'GYRO-Z-KURT-Ring1', 'ACC-X-KURT-Ring2', 'ACC-Y-KURT-Ring2', 'ACC-Z-KURT-Ring2', 'GYRO-X-KURT-Ring2',
             'GYRO-Y-KURT-Ring2', 'GYRO-Z-KURT-Ring2'],
            axis=1, inplace=False)
        return kurt_df_3

    def kurtosis_df():
        kurt_df = kurtosis(grouped.get_group(1).drop(columns="TEST"))
        # print(min_df)
        for group in range(grouped.ngroups - 1):
            kurt_df = kurt_df.append(kurtosis(grouped.get_group(group + 2).drop(columns="TEST")), ignore_index=True)
            # max_df = pd.concat()
        return kurt_df

    c_df = min_df().join(max_df()).join(mean_df()).join(variance_df()).join(skewness_df()).join(kurtosis_df())
    c_df.insert(0, 'GESTURE', test_type)

    # print(c_df)

    return c_df
