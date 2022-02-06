import pandas as pd


def dataframe_merging(data_frame1, data_frame2, data_frame3, data_frame4, data_frame5, data_frame6):
    frames = [data_frame1, data_frame2, data_frame3, data_frame4, data_frame5, data_frame6]
    result = pd.concat(frames)
    return result
