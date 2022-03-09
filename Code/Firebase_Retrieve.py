import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from Real_Time_FE import *
from KNN_Train import *
from KNN_Predict import *
import pandas as pd
#from threading import Thread
import time
import threading

start = time.perf_counter()
predictor = KNN_train()

# Connect to Firebase
cred = credentials.Certificate(
    '../FirebaseKey/fingergesturerecognitionsystem-firebase-adminsdk-xcpqf-cf83d06251.json')  # get service account key JSON
# Initialize with service account to get admin privileges
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fingergesturerecognitionsystem-default-rtdb.firebaseio.com/"
})

headers = ['ACC-X', 'ACC-Y', 'ACC-Z', 'GYRO-X', 'GYRO-Y', 'GYRO-Z', 'TEST']
df = pd.DataFrame(columns=headers)

#t1 = threading.Thread(target=RT_FE)
#t2 = threading.Thread(target=KNN_predict)

def listener(event):
    if event.path == "/":
        print("SKIP")

    elif event.path == "/TEST":
        del event.data[0]
        # df.insert(0, "TEST", event.data)
        df['TEST'] = event.data

    elif event.path == "/ACC-X":
        del event.data[0]
        df['ACC-X'] = event.data

    elif event.path == "/ACC-Y":
        del event.data[0]
        df['ACC-Y'] = event.data

    elif event.path == "/ACC-Z":
        del event.data[0]
        df['ACC-Z'] = event.data

    elif event.path == "/GYRO-X":
        del event.data[0]
        df['GYRO-X'] = event.data

    elif event.path == "/GYRO-Y":
        del event.data[0]
        df['GYRO-Y'] = event.data

    elif event.path == "/GYRO-Z":
        del event.data[0]
        df['GYRO-Z'] = event.data
        print(df)
        fe = RT_FE(df, "WTV", "ring1")
        print("FEATURE EXTRACTION: ")
        print(fe)

       # KNN_predict(predictor, fe)
       # t1.start()
       # t2.start()

       # t1.join()
        #t2.join()

        finish = time.perf_counter()
        print(f'Finished in {round(finish-start, 2)} second')

    else:
        print("OH OH SMTH WRONG HAPPENED WOOPSIES: ", str(event.path), " :", str(event.data))


ring2 = firebase_admin.db.reference('Ring2').listen(listener)




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
