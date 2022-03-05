import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


def KNN_train():
    # Create feature and target arrays
    X = pd.read_csv('../DataSet/extracted_features.csv').drop("GESTURE", axis=1)
    # print("X: " + str(X))
    y = pd.read_csv('../DataSet/extracted_features.csv', usecols=['GESTURE'])
    # print("y: " + str(y))

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

    score = grid_fit.best_score_
    score_percent = float(score) * 100
    print("Training Score: ", str(score_percent) + "%")

    return best_knn
