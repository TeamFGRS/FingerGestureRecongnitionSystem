import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from DF_to_CSV import *
import pandas as pd
import threading

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
testCounter = 1
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


def inc_test_counter():
    global testCounter
    lock.acquire()
    testCounter += 1
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
        test = [testCounter] * 20
        df['TEST'] = test

    elif event.path == "/Ring2/TEST":
        test = [testCounter] * 20
        df['TEST'] = test

    elif event.path == "/Ring1/ACC-X":
        del event.data[0]
        print("ACC-X-Ring1: ", str(event.data))
        df['ACC-X-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/ACC-X":
        del event.data[0]
        print("ACC-X-Ring2: ", str(event.data))
        df['ACC-X-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/ACC-Y":
        del event.data[0]
        print("ACC-Y-Ring1: ", str(event.data))
        df['ACC-Y-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/ACC-Y":
        del event.data[0]
        print("ACC-Y-Ring2: ", str(event.data))
        df['ACC-Y-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/ACC-Z":
        del event.data[0]
        print("ACC-Z-Ring1: ", str(event.data))
        df['ACC-Z-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/ACC-Z":
        del event.data[0]
        print("ACC-Z-Ring2: ", str(event.data))
        df['ACC-Z-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/GYRO-X":
        del event.data[0]
        print("GYRO-X-Ring1: ", str(event.data))
        df['GYRO-X-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/GYRO-X":
        del event.data[0]
        print("GYRO-X-Ring2: ", str(event.data))
        df['GYRO-X-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/GYRO-Y":
        del event.data[0]
        print("GYRO-Y-Ring1: ", str(event.data))
        df['GYRO-Y-Ring1'] = event.data
        update_counter()

    elif event.path == "/Ring2/GYRO-Y":
        del event.data[0]
        print("GYRO-Y-Ring2: ", str(event.data))
        df['GYRO-Y-Ring2'] = event.data
        update_counter()

    elif event.path == "/Ring1/GYRO-Z":
        del event.data[0]
        print("GYRO-Z-Ring1: ", str(event.data))
        df['GYRO-Z-Ring1'] = event.data
        update_counter()

        print("Check at GYRO-Z RING1: ", str(detectionCounter))
        if detectionCounter == 12:
            print(df)
            df_to_csv(df, "../DataSet2/test.csv")
            reset_counter()
            print("Check reset at GYRO-Z RING1: ", str(detectionCounter))
            inc_test_counter()

    elif event.path == "/Ring2/GYRO-Z":
        del event.data[0]
        print("GYRO-Z-Ring2: ", str(event.data))
        df['GYRO-Z-Ring2'] = event.data

        update_counter()
        print("Check at GYRO-Z RING2: ", str(detectionCounter))
        if detectionCounter == 12:
            print(df)
            df_to_csv(df, "../DataSet2/test.csv")
            reset_counter()
            print("Check reset at GYRO-Z RING2: ", str(detectionCounter))
            inc_test_counter()


    else:
        print("OTHER: ", str(event.path), " :", str(event.data))
        if detectionCounter != 0:
            print("Counter at OTHER: ", str(detectionCounter))
            reset_counter()
            print("Check reset at OTHER: ", str(detectionCounter))


ring1 = firebase_admin.db.reference('/').listen(listener)
