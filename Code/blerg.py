import os
import sys

import serial
import pandas as pd

arduinoData = serial.Serial("com3", 115220)

accelX = []
accelY = []
accelZ = []
gyroX = []
gyroY = []
gyroZ = []
test = []

count = 0

while True:
    while arduinoData.inWaiting() == 0:
        pass

    path_file = "../DataSet/demo.csv"
    input_data = arduinoData.readline().strip().decode("utf-8")
    dataArray = input_data.split(',')

    aX = float(dataArray[0])
    aY = float(dataArray[1])
    aZ = float(dataArray[2])
    gX = float(dataArray[3])
    gY = float(dataArray[4])
    gZ = float(dataArray[5])
    t = int(dataArray[6])

    accelX.append(aX)
    accelY.append(aY)
    accelZ.append(aZ)
    gyroX.append(gX)
    gyroY.append(gY)
    gyroZ.append(gZ)
    test.append(t)

    count = count + 1

    if count > 200:
        sys.exit()
        # accelX.clear()
        # accelY.clear()
        # accelZ.clear()
        # gyroX.clear()
        # gyroY.clear()
        # gyroZ.clear()
        # test.clear()
        # count = 0




    df = pd.DataFrame(list(zip(accelX, accelY, accelZ, gyroX, gyroY, gyroZ, test)),
                      columns=['ACC-X', 'ACC-Y', 'ACC-Z', 'GYRO-X', 'GYRO-Y', 'GYRO-Z', 'TEST'])

    print(df)

    path_file = "../DataSet/blerg.csv"

    if not os.path.isfile(path_file):
        df.to_csv(path_file, index=False, header=True)
    else:
        df.to_csv(path_file, mode='w', index=False, header=False)
