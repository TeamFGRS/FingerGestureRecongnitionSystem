import pandas as pd


def read_file(data_file):
    d_file = pd.read_csv(data_file,
                         usecols=['ACC-X', 'ACC-Y', 'ACC-Z', 'GYRO-X', 'GYRO-Y', 'GYRO-Z', 'TEST'])
    print(d_file)
    return d_file.dropna()
