import pandas as pd
import os


def df_to_csv(df, path):
    path_file = path

    if not os.path.isfile(path_file):
        df.to_csv(path_file, index=False, header=True)
    else:
        df.to_csv(path_file, mode='a', index=False, header=False)

    return 1
