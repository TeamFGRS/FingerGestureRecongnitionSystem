import pandas as pd

from Sensor_Data_Reader import *
from Feature_Extraction import *
from Data_Frame_Merging import *
from DF_to_CSV import *

# finger up data frame
fingerUp = read_file('../DataSet/up_gesture.csv')
# finger down data frame
fingerDown = read_file('../DataSet/down_gesture.csv')
# finger left data frame
fingerLeft = read_file('../DataSet/left_gesture.csv')
# finger right data frame
fingerRight = read_file('../DataSet/right_gesture.csv')
# 90 deg clock data frame
fingerClock = read_file('../DataSet/clock_gesture.csv')
# 90 deg counter data frame
fingerCounter = read_file('../DataSet/counter_gesture.csv')

# run feature extraction
up_df = feature_extraction(fingerUp, "up", "ring1")
down_df = feature_extraction(fingerDown, "down", "ring1")
right_df = feature_extraction(fingerRight, "right", "ring1")
left_df = feature_extraction(fingerLeft, "left", "ring1")
clock_df = feature_extraction(fingerClock, "clock", "ring1")
counter_df = feature_extraction(fingerCounter, "counter", "ring1")

# merge features into one data frame
f_df = dataframe_merging(up_df, down_df, right_df, left_df, clock_df,counter_df)

# store into file
df_to_csv(f_df, "../DataSet/extracted_features.csv")
