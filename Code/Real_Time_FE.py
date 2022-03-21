import pandas as pd


def RT_FE(grouped):
    # def minimum(data_group):
    #     min_df = data_group.min().to_frame().transpose()
    #     min_df_2 = min_df.reset_index(drop=True)
    #     min_df_3 = min_df_2.set_axis(
    #         ['ACC-X-MIN-Ring1', 'ACC-Y-MIN-Ring1', 'ACC-Z-MIN-Ring1', 'GYRO-X-MIN-Ring1', 'GYRO-Y-MIN-Ring1',
    #          'GYRO-Z-MIN-Ring1', 'ACC-X-MIN-Ring2', 'ACC-Y-MIN-Ring2', 'ACC-Z-MIN-Ring2', 'GYRO-X-MIN-Ring2',
    #          'GYRO-Y-MIN-Ring2', 'GYRO-Z-MIN-Ring2', 'ACC-X-MIN-Ring3', 'ACC-Y-MIN-Ring3', 'ACC-Z-MIN-Ring3',
    #          'GYRO-X-MIN-Ring3', 'GYRO-Y-MIN-Ring3', 'GYRO-Z-MIN-Ring3'],
    #         axis=1, inplace=False)
    #     return min_df_3
    #
    # def min_df():
    #     min_df = minimum(grouped.drop(columns="TEST"))
    #     return min_df
    #
    # def maximum(data_group):
    #     max_df = data_group.max().to_frame().transpose()
    #     max_df_2 = max_df.reset_index(drop=True)
    #     max_df_3 = max_df_2.set_axis(
    #         ['ACC-X-MAX-Ring1', 'ACC-Y-MAX-Ring1', 'ACC-Z-MAX-Ring1', 'GYRO-X-MAX-Ring1', 'GYRO-Y-MAX-Ring1',
    #          'GYRO-Z-MAX-Ring1', 'ACC-X-MAX-Ring2', 'ACC-Y-MAX-Ring2', 'ACC-Z-MAX-Ring2', 'GYRO-X-MAX-Ring2',
    #          'GYRO-Y-MAX-Ring2', 'GYRO-Z-MAX-Ring2', 'ACC-X-MAX-Ring3', 'ACC-Y-MAX-Ring3', 'ACC-Z-MAX-Ring3',
    #          'GYRO-X-MAX-Ring3', 'GYRO-Y-MAX-Ring3', 'GYRO-Z-MAX-Ring3'],
    #         axis=1, inplace=False)
    #     return max_df_3
    #
    # def max_df():
    #     max_df = maximum(grouped.drop(columns="TEST"))
    #     return max_df

    def median(data_group):
        median_df = data_group.median().to_frame().transpose()
        median_df_2 = median_df.reset_index(drop=True)
        median_df_3 = median_df_2.set_axis(
            ['ACC-X-MED-Ring1', 'ACC-Y-MED-Ring1', 'ACC-Z-MED-Ring1', 'GYRO-X-MED-Ring1', 'GYRO-Y-MED-Ring1',
             'GYRO-Z-MED-Ring1', 'ACC-X-MED-Ring2', 'ACC-Y-MED-Ring2', 'ACC-Z-MED-Ring2', 'GYRO-X-MED-Ring2',
             'GYRO-Y-MED-Ring2', 'GYRO-Z-MED-Ring2', 'ACC-X-MED-Ring3', 'ACC-Y-MED-Ring3', 'ACC-Z-MED-Ring3',
             'GYRO-X-MED-Ring3', 'GYRO-Y-MED-Ring3', 'GYRO-Z-MED-Ring3'],
            axis=1, inplace=False)
        return median_df_3

    def median_df():
        median_df = median(grouped.drop(columns="TEST"))
        return median_df

    # def mean(data_group):
    #     mean_df = data_group.mean().to_frame().transpose()
    #     mean_df_2 = mean_df.reset_index(drop=True)
    #     mean_df_3 = mean_df_2.set_axis(
    #         ['ACC-X-MEAN-Ring1', 'ACC-Y-MEAN-Ring1', 'ACC-Z-MEAN-Ring1', 'GYRO-X-MEAN-Ring1', 'GYRO-Y-MEAN-Ring1',
    #          'GYRO-Z-MEAN-Ring1', 'ACC-X-MEAN-Ring2', 'ACC-Y-MEAN-Ring2', 'ACC-Z-MEAN-Ring2', 'GYRO-X-MEAN-Ring2',
    #          'GYRO-Y-MEAN-Ring2', 'GYRO-Z-MEAN-Ring2', 'ACC-X-MEAN-Ring3', 'ACC-Y-MEAN-Ring3', 'ACC-Z-MEAN-Ring3',
    #          'GYRO-X-MEAN-Ring3', 'GYRO-Y-MEAN-Ring3', 'GYRO-Z-MEAN-Ring3'],
    #         axis=1, inplace=False)
    #     return mean_df_3
    #
    # def mean_df():
    #     mean_df = mean(grouped.drop(columns="TEST"))
    #     return mean_df

    def standard_deviation(data_group):
        std_df = data_group.std(ddof=0).to_frame().transpose()
        std_df_2 = std_df.reset_index(drop=True)
        std_df_3 = std_df_2.set_axis(
            ['ACC-X-STD-Ring1', 'ACC-Y-STD-Ring1', 'ACC-Z-STD-Ring1', 'GYRO-X-STD-Ring1', 'GYRO-Y-STD-Ring1',
             'GYRO-Z-STD-Ring1', 'ACC-X-STD-Ring2', 'ACC-Y-STD-Ring2', 'ACC-Z-STD-Ring2', 'GYRO-X-STD-Ring2',
             'GYRO-Y-STD-Ring2', 'GYRO-Z-STD-Ring2', 'ACC-X-STD-Ring3', 'ACC-Y-STD-Ring3', 'ACC-Z-STD-Ring3',
             'GYRO-X-STD-Ring3', 'GYRO-Y-STD-Ring3', 'GYRO-Z-STD-Ring3'],
            axis=1, inplace=False)
        return std_df_3

    def standard_deviation_df():
        std_df = standard_deviation(grouped.drop(columns="TEST"))

        return std_df

    def variance(data_group):
        var_df = data_group.var(ddof=0).to_frame().transpose()
        var_df_2 = var_df.reset_index(drop=True)
        var_df_3 = var_df_2.set_axis(
            ['ACC-X-VAR-Ring1', 'ACC-Y-VAR-Ring1', 'ACC-Z-VAR-Ring1', 'GYRO-X-VAR-Ring1', 'GYRO-Y-VAR-Ring1',
             'GYRO-Z-VAR-Ring1', 'ACC-X-VAR-Ring2', 'ACC-Y-VAR-Ring2', 'ACC-Z-VAR-Ring2', 'GYRO-X-VAR-Ring2',
             'GYRO-Y-VAR-Ring2', 'GYRO-Z-VAR-Ring2', 'ACC-X-VAR-Ring3', 'ACC-Y-VAR-Ring3', 'ACC-Z-VAR-Ring3',
             'GYRO-X-VAR-Ring3', 'GYRO-Y-VAR-Ring3', 'GYRO-Z-VAR-Ring3'],
            axis=1, inplace=False)
        return var_df_3

    def variance_df():
        var_df = variance(grouped.drop(columns="TEST"))
        return var_df

    def skewness(data_group):
        skew_df = data_group.skew().to_frame().transpose()
        skew_df_2 = skew_df.reset_index(drop=True)
        skew_df_3 = skew_df_2.set_axis(
            ['ACC-X-SKEW-Ring1', 'ACC-Y-SKEW-Ring1', 'ACC-Z-SKEW-Ring1', 'GYRO-X-SKEW-Ring1', 'GYRO-Y-SKEW-Ring1',
             'GYRO-Z-SKEW-Ring1', 'ACC-X-SKEW-Ring2', 'ACC-Y-SKEW-Ring2', 'ACC-Z-SKEW-Ring2', 'GYRO-X-SKEW-Ring2',
             'GYRO-Y-SKEW-Ring2', 'GYRO-Z-SKEW-Ring2', 'ACC-X-SKEW-Ring3', 'ACC-Y-SKEW-Ring3', 'ACC-Z-SKEW-Ring3',
             'GYRO-X-SKEW-Ring3', 'GYRO-Y-SKEW-Ring3', 'GYRO-Z-SKEW-Ring3'],
            axis=1, inplace=False)
        return skew_df_3

    def skewness_df():
        skew_df = skewness(grouped.drop(columns="TEST"))
        return skew_df

    def kurtosis(data_group):
        kurt_df = data_group.kurtosis().to_frame().transpose()
        kurt_df_2 = kurt_df.reset_index(drop=True)
        kurt_df_3 = kurt_df_2.set_axis(
            ['ACC-X-KURT-Ring1', 'ACC-Y-KURT-Ring1', 'ACC-Z-KURT-Ring1', 'GYRO-X-KURT-Ring1', 'GYRO-Y-KURT-Ring1',
             'GYRO-Z-KURT-Ring1', 'ACC-X-KURT-Ring2', 'ACC-Y-KURT-Ring2', 'ACC-Z-KURT-Ring2', 'GYRO-X-KURT-Ring2',
             'GYRO-Y-KURT-Ring2', 'GYRO-Z-KURT-Ring2', 'ACC-X-KURT-Ring3', 'ACC-Y-KURT-Ring3', 'ACC-Z-KURT-Ring3',
             'GYRO-X-KURT-Ring3', 'GYRO-Y-KURT-Ring3', 'GYRO-Z-KURT-Ring3'],
            axis=1, inplace=False)
        return kurt_df_3

    def kurtosis_df():
        kurt_df = kurtosis(grouped.drop(columns="TEST"))
        return kurt_df

    c_df = median_df().join(standard_deviation_df()).join(variance_df()).join(skewness_df()).join(kurtosis_df())

    return c_df
