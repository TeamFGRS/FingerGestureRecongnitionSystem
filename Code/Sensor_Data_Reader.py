import pandas as pd


def read_file(data_file):
    d_file = pd.read_csv(data_file, low_memory=False,
                         usecols=['GYRO-X-Ring1', 'GYRO-Y-Ring1', 'GYRO-Z-Ring1', 'GYRO-X-Ring2', 'GYRO-Y-Ring2',
                                  'GYRO-Z-Ring2', 'GYRO-X-Ring3', 'GYRO-Y-Ring3', 'GYRO-Z-Ring3', 'TEST'])
    return pd.DataFrame(d_file.dropna())


