import serial
import io
import pandas as pd

arduinoData = serial.Serial("com3", 115220)

counter = 0
test_counter = 0

while True:
    while arduinoData.inWaiting() == 0:
        pass

    path_file = "../DataSet/testing_gestures.csv"

    if counter == 0:
        input_data = "ACC-X,ACC-Y,ACC-Z,GYRO-X,GYRO-Y,GYRO-Z,TEST"
        counter = counter + 1
    else:
        input_data = arduinoData.readline().strip().decode("utf-8")
    if input_data != "":
        print(input_data)
        test_counter = test_counter + 1

    with open(path_file, "a") as myfile:
        myfile.write(input_data + "\n")
