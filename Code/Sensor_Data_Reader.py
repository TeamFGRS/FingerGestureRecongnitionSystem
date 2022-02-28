import pandas as pd


def read_file(data_file):
    d_file = pd.read_csv(data_file, low_memory=False,
                         usecols=['ACC-X', 'ACC-Y', 'ACC-Z', 'GYRO-X', 'GYRO-Y', 'GYRO-Z', 'TEST'])
    return pd.DataFrame(d_file.dropna())


