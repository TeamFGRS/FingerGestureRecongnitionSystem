import pandas as pd


def read_file(data_file):
    d_file = pd.read_csv(data_file, low_memory=False,
                         usecols=['ACC-X-Ring1', 'ACC-Y-Ring1', 'ACC-Z-Ring1', 'GYRO-X-Ring1', 'GYRO-Y-Ring1',
                                  'GYRO-Z-Ring1', 'ACC-X-Ring2', 'ACC-Y-Ring2', 'ACC-Z-Ring2', 'GYRO-X-Ring2',
                                  'GYRO-Y-Ring2', 'GYRO-Z-Ring2', 'TEST'])
    return pd.DataFrame(d_file.dropna())


