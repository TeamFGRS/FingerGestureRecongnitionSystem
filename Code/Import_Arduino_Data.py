import serial

ser = serial.Serial("/dev/cu.usbmodem1101", 115200, timeout=1)
counter = 0
test_counter = 0
while True:
    if ser.isOpen():
        if counter == 0:
            input_data = "ACC-X,ACC-Y,ACC-Z,GYRO-X,GYRO-Y,GYRO-Z,TEST"
            counter = counter + 1
        else:
            input_data = ser.readline().strip().decode("utf-8")
        if input_data != "":
            print(input_data)
            test_counter = test_counter + 1




# # ARDUINO PORT DIRECTORY
# arduino_port = "/dev/cu.usbmodem1101"
# baud = 115200
# new_file = "../DataSet/arduino_readings.csv"
#
# # TO BE CHANGED
# sample_data = 1200
# print_labels = False
# line = 0
#
# serial_port = serial.Serial(arduino_port, baud)
# print("Connected to Arduino port:" + arduino_port)
# file = open(new_file, "a")
# print("Created file")
# #
# # #display the data to the terminal
# # getData = str(serial_port.readline())
# # data = getData[0:][:-2]
# # print(data)
# #
# # #add the data to the file
# # file = open(new_file, "a") #append the data to the file
# # file.write(data + "\n") #write data with a newline
# #
# # #close out the file
# # file.close()
#
# while line <= sample_data:
#     if print_labels:
#         if line == 0:
#             print("Printing Column Headers")
#         else:
#             print("Line " + str(line) + ": writing...")
#     getData = str(serial_port.readline())
#     data = getData[0:][:-2]
#     print(data)
#
#     file = open(new_file, "a")
#     # write data with a newline
#     file.write(data + "\n")
#     line = line + 1
#
# print("Data collection complete!")
# file.close()
