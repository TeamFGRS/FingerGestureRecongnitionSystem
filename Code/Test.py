from Sensor_Data_Reader import *
from Feature_Extraction import *

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

feature_extraction(fingerUp, "up", "ring1")
