import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from Real_Time_FE import *
from KNN_TP import *
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
test1 = 0
test2 = 0


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

def updateTest1(test):
    global test1
    lock.acquire()
    test1 = test
    print("TEST1", str(test1))
    lock.release()


def updateTest2(test):
    global test2
    lock.acquire()
    test2 = test
    print("TEST2", str(test2))
    lock.release()


def listener(event):
    if event.path == "/":
        print("SKIP")

    elif event.path == "/Ring1/TEST":
        del event.data[0]
        df['TEST'] = event.data
        list = event.data
        updateTest1(list[2])

    elif event.path == "/Ring2/TEST":
        del event.data[0]
        df['TEST'] = event.data
        list = event.data
        updateTest2(list[2])

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
        if detectionCounter == 12 and test1 == test2:
            print(df)
            reset_counter()
            print("Check reset at GYRO-Z RING1: ", str(detectionCounter))
            fe = RT_FE(df)
            print("FEATURE EXTRACTION: ")
            print(fe)
            KNN_predict(predictor, fe)

    elif event.path == "/Ring2/GYRO-Z":
        del event.data[0]
        df['GYRO-Z-Ring2'] = event.data
        update_counter()
        print("Check at GYRO-Z RING2: ", str(detectionCounter))
        if detectionCounter == 12 and test1 == test2:
            print(df)
            reset_counter()
            print("Check reset at GYRO-Z RING2: ", str(detectionCounter))
            fe = RT_FE(df)
            print("FEATURE EXTRACTION: ")
            print(fe)
            KNN_predict(predictor, fe)

    else:
        print("OTHER: ", str(event.path), " :", str(event.data))
        if detectionCounter != 0:
            print("Counter at OTHER: ", str(detectionCounter))
            reset_counter()
            print("Check reset at OTHER: ", str(detectionCounter))


ring1 = firebase_admin.db.reference('/').listen(listener)
