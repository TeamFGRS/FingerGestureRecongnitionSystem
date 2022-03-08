import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from Real_Time_FE import *
from KNN_Train import *
from KNN_Predict import *
import pandas as pd
import threading

predictor = KNN_train()

# Connect to Firebase
cred = credentials.Certificate(
    '../FirebaseKey/fingergesturerecognitionsystem-firebase-adminsdk-xcpqf-cf83d06251.json')  # get service account key JSON
# Initialize with service account to get admin privileges
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fingergesturerecognitionsystem-default-rtdb.firebaseio.com/"
})

headers = ['ACC-X-Ring1', 'ACC-Y-Ring1', 'ACC-Z-Ring1', 'GYRO-X-Ring1', 'GYRO-Y-Ring1', 'GYRO-Z-Ring1', 'ACC-X-Ring2',
           'ACC-Y-Ring2', 'ACC-Z-Ring2', 'GYRO-X-Ring2', 'GYRO-Y-Ring2', 'GYRO-Z-Ring2', 'TEST']
df = pd.DataFrame(columns=headers)

lock = threading.Lock()
detectionCounter = 0


def update_counter():
    global detectionCounter
    lock.acquire()
    detectionCounter += 1
    lock.release()


def reset_counter():
    global detectionCounter
    lock.acquire()
    detectionCounter = 0
    lock.release()


def listener(event):
    if event.path == "/":
        print("SKIP")

    elif event.path == "/Ring1/TEST":
        del event.data[0]
        # df.insert(0, "TEST", event.data)
        df['TEST'] = event.data

    elif event.path == "/Ring2/TEST":
        del event.data[0]
        df['TEST'] = event.data

    elif event.path == "/Ring1/ACC-X":
        del event.data[0]
        df['ACC-X-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/ACC-X":
        del event.data[0]
        df['ACC-X-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/ACC-Y":
        del event.data[0]
        df['ACC-Y-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/ACC-Y":
        del event.data[0]
        df['ACC-Y-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/ACC-Z":
        del event.data[0]
        df['ACC-Z-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/ACC-Z":
        del event.data[0]
        df['ACC-Z-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/GYRO-X":
        del event.data[0]
        df['GYRO-X-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/GYRO-X":
        del event.data[0]
        df['GYRO-X-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/GYRO-Y":
        del event.data[0]
        df['GYRO-Y-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/GYRO-Y":
        del event.data[0]
        df['GYRO-Y-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/GYRO-Z":
        del event.data[0]
        df['GYRO-Z-Ring1'] = event.data
        update_counter()
        print("Check at GYRO-Z RING1: ", str(detectionCounter))
        if detectionCounter == 12:
            print(df)
            reset_counter()
            print("Check reset at GYRO-Z RING1: ", str(detectionCounter))
            fe = RT_FE(df)
            print("FEATURE EXTRACTION: ")
            print(fe)
            # KNN_predict(predictor, fe)

    elif event.path == "/Ring2/GYRO-Z":
        del event.data[0]
        df['GYRO-Z-Ring2'] = event.data
        update_counter()
        print("Check at GYRO-Z RING2: ", str(detectionCounter))
        if detectionCounter == 12:
            print(df)
            reset_counter()
            print("Check reset at GYRO-Z RING2: ", str(detectionCounter))
            fe = RT_FE(df)
            print("FEATURE EXTRACTION: ")
            print(fe)
            # KNN_predict(predictor, fe)

    else:
        print("OTHER: ", str(event.path), " :", str(event.data))


ring1 = firebase_admin.db.reference('/').listen(listener)

# print("LIST")
# print(*gyroX)
# print("END OF LIST")
# gyroX.clear()

# # PUT IN DATAFRAME
# df = pd.DataFrame.from_dict(data, orient='index')
# #df_grouped = df.groupby(df.index)
# df_grouped=df.groupby(df.index).apply(print)

# def listener(event):
#     # print(event.event_type)  # can be 'put' or 'patch'
#     # print(event.path)  # relative to the reference, it seems
#     print(event.data)  # new data at /reference/event.path. None if deleted
