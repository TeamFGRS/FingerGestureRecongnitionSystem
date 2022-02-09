from Sensor_Data_Reader import *
from Feature_Extraction import *
from Data_Frame_Merging import *
from DF_to_CSV import *

# extracted features
testData = read_file('../DataSet/test_data.csv')

random_df = feature_extraction(testData, "random", "ring1")
df_to_csv(random_df)
