import pandas as pd

from Sensor_Data_Reader import *
from DS_Feature_Extraction import *
from Data_Frame_Merging import *
from DF_to_CSV import *

# finger up data frame
fingerUp = read_file('../DataSet3/up.csv')
# finger down data frame
fingerDown = read_file('../DataSet3/down.csv')
# finger left data frame
fingerLeft = read_file('../DataSet3/left.csv')
# finger right data frame
fingerRight = read_file('../DataSet3/right.csv')
# 90 deg clock data frame
fingerClock = read_file('../DataSet3/clock.csv')
# 90 deg counter data frame
fingerCounter = read_file('../DataSet3/counter.csv')

# run feature extraction
up_df = feature_extraction(fingerUp, "up")
down_df = feature_extraction(fingerDown, "down")
right_df = feature_extraction(fingerRight, "right")
left_df = feature_extraction(fingerLeft, "left")
clock_df = feature_extraction(fingerClock, "clock")
counter_df = feature_extraction(fingerCounter, "counter")

# merge features into one data frame
f_df = dataframe_merging(up_df, down_df, right_df, left_df, clock_df, counter_df)

# store into file
df_to_csv(f_df, "../DataSet3/extracted_features.csv")
