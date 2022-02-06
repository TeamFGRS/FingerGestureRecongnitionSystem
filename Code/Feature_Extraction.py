import pandas as pd


def feature_extraction(data_file, test_type, ring_number):
    # TODO: autocovariance(?), maybe fix warnings

    features = pd.DataFrame(data_file)
    grouped = features.groupby(features["TEST"])

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

    c_df = min_df().join(max_df()).join(mean_df()).join(variance_df()).join(skewness_df()).join(kurtosis_df())
    c_df.insert(0, 'GESTURE', test_type)

    # print(c_df)

    return c_df
