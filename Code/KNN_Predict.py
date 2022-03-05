import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection  import GridSearchCV


def KNN_predict(predictor, df):

    Z = df.drop(columns='GESTURE')

    print("Best predictions Grid search:")
    print(predictor.predict(Z))