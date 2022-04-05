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
# snap data frame
fingerSnap = read_file('../DataSet3/snap.csv')
# # pinch in data frame
# fingerPIn = read_file('../DataSet3/pinch_in.csv')
# # pinch out data frame
# fingerPOut = read_file('../DataSet3/pinch_out.csv')
# ignore data frame
fingerIgnore = read_file('../DataSet3/ignore.csv')
# reset data frame
fingerReset = read_file('../DataSet3/reset.csv')


# run feature extraction
up_df = feature_extraction(fingerUp, "up")
down_df = feature_extraction(fingerDown, "down")
right_df = feature_extraction(fingerRight, "right")
left_df = feature_extraction(fingerLeft, "left")
clock_df = feature_extraction(fingerClock, "clock")
counter_df = feature_extraction(fingerCounter, "counter")
snap_df = feature_extraction(fingerSnap, "snap")
# pin_df = feature_extraction(fingerPIn, "pinch_in")
# pout_df = feature_extraction(fingerPOut, "pinch_out")
ignore_df = feature_extraction(fingerIgnore, "ignore")
reset_df = feature_extraction(fingerReset, "reset")


# # merge features into one data frame
# f_df = dataframe_merging(up_df, down_df, right_df, left_df, clock_df, counter_df, snap_df, pin_df, pout_df)

# merge features into one data frame
f_df = dataframe_merging(up_df, down_df, right_df, left_df, clock_df, counter_df, snap_df, ignore_df, reset_df)

# store into file
df_to_csv(f_df, "../DataSet3/extracted_features.csv")
