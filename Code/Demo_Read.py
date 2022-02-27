import serial
import sys

arduinoData = serial.Serial("com3", 115220)

count = 0

while True:
    while arduinoData.inWaiting() == 0:
        pass

    path_file = "../DataSet/demo.csv"
    input_data = arduinoData.readline().strip().decode("utf-8")

    with open(path_file, "a") as myfile:
        myfile.write(input_data + "\n")

    count = count + 1

    print(input_data)

    if count > 200:
        sys.exit()