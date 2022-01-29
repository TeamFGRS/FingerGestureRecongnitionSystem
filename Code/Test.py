from Sensor_Data_Reader import *
from Feature_Extraction import *
from Data_Frame_Merging import *
from DF_to_CSV import *

# finger up file
fingerUp = read_file('../DataSet/Finger_up.csv')
# finger down
fingerDown = read_file('../DataSet/Finger_down.csv')
# finger left
fingerLeft = read_file('../DataSet/Finger_Left.csv')
# finger right
fingerRight = read_file('../DataSet/Finger_right.csv')
# 90 deg clock
fingerClock = read_file('../DataSet/90deg_clockwise.csv')
# 90 deg counter
fingerCounter = read_file('../DataSet/90deg_counter_clockwise.csv')
# extracted features
# extractedFeatures = read_file('../DataSet/extracted_features.csv')

up_df = feature_extraction(fingerUp, "up", "ring1")
down_df = feature_extraction(fingerDown, "down", "ring1")
right_df = feature_extraction(fingerRight, "right", "ring1")
left_df = feature_extraction(fingerLeft, "left", "ring1")
# clock_df = feature_extraction(fingerClock, "clock", "ring1")
counter_df = feature_extraction(fingerCounter, "counter", "ring1")

f_df = dataframe_merging(up_df, down_df, right_df, left_df, counter_df)
df_to_csv(f_df)
