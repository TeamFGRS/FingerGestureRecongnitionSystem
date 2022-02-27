import serial
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from DF_to_CSV import *
from Feature_Extraction import *

arduinoData = serial.Serial("com3", 115220)

accelX = []
accelY = []
accelZ = []
gyroX = []
gyroY = []
gyroZ = []
test = []


# Read Sensor Arduino
def arduino(arduino):
    # Read Arduino
    count = 0
    while arduino.inWaiting() == 0:
        pass
    path_file = "../DataSet/demo.csv"
    input_data = arduino.readline().strip().decode("utf-8")
    dataArray = input_data.split(',')

    aX = float(dataArray[0])
    aY = float(dataArray[1])
    aZ = float(dataArray[2])
    gX = float(dataArray[3])
    gY = float(dataArray[4])
    gZ = float(dataArray[5])
    t = float(dataArray[6])

    accelX.append(aX)
    accelY.append(aY)
    accelZ.append(aZ)
    gyroX.append(gX)
    gyroY.append(gY)
    gyroZ.append(gZ)
    test.append(t)

    count = count + 1

    df = pd.DataFrame(list(zip(accelX, accelY, accelZ, gyroX, gyroY, gyroZ, test)),
                      columns=['ACC-X', 'ACC-Y', 'ACC-Z', 'GYRO-X', 'GYRO-Y', 'GYRO-Z', 'TEST'])

    if count > 200:
        return df
        # accelX.clear()
        # accelY.clear()
        # accelZ.clear()
        # gyroX.clear()
        # gyroY.clear()
        # gyroZ.clear()
        # test.clear()
        # count = 0


def featured_extraction_csv(df):
    path_file = "../DataSet/demo_features_extracted.csv"

    if not os.path.isfile(path_file):
        df.to_csv(path_file, index=False, header=True)
    else:
        df.to_csv(path_file, mode='w', index=False, header=False)

    return path_file


# KNN
def training():
    # Create feature and target arrays
    X = pd.read_csv('../DataSet/extracted_features.csv').drop("GESTURE", axis=1)
    y = pd.read_csv('../DataSet/extracted_features.csv', usecols=['GESTURE'])

    # Split into training and test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=3)

    parameters = {'n_neighbors': [5, 6, 7],
                  'weights': ['uniform', 'distance'],
                  'p': [1, 2]}

    grid_obj = GridSearchCV(knn, param_grid=parameters,
                            verbose=1, cv=3, n_jobs=-1)

    grid_fit = grid_obj.fit(X_train, y_train.values.ravel())
    best_knn = grid_fit.best_estimator_
    return best_knn


def knn(predictor, gesture_df):
    Z = gesture_df.drop("GESTURE", 1)
    best_prediction = predictor.predict(Z)
    print(best_prediction)


def main():
    while True:
        predictor = training()
        dataframe = arduino(arduinoData)
        print(dataframe)
        demoData = feature_extraction(dataframe, "random", "ring1")
        # featured_path = featured_extraction_csv(demoData)
        knn(predictor, demoData)


if __name__ == "__main__":
    main()
