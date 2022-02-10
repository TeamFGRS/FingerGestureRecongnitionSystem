import serial
import io
import pandas as pd

arduinoData = serial.Serial("com3", 115220)
try:
    while True:
        while arduinoData.inWaiting() == 0:
            pass

        arduinoDataString = arduinoData.readline().strip().decode("utf-8")

        path_file = "../DataSet/up_gesture.csv"
        header = "ACC-X,ACC-Y,ACC-Z,GYRO-X,GYRO-Y,GYRO-Z,TEST"



        print(df)
except KeyboardInterrupt:
    pass