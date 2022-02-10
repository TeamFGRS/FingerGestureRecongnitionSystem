import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection  import GridSearchCV
from sklearn.datasets import load_iris


# Loading data

# Create feature and target arrays
X = pd.read_csv('../DataSet/extracted_features.csv').drop("GESTURE", axis=1)
print("X: "+str(X))
y = pd.read_csv('../DataSet/extracted_features.csv', usecols=['GESTURE'])
print("y: "+str(y))

Z = pd.read_csv('../DataSet/testing_features.csv').drop("GESTURE", axis=1)

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

parameters = {'n_neighbors' : [5, 6, 7],
              'weights': ['uniform', 'distance'],
              'p': [1, 2]}

grid_obj = GridSearchCV(knn, param_grid=parameters,
                        verbose=1, cv=3, n_jobs=-1)

#knn.fit(X_train, y_train.values.ravel())

grid_fit = grid_obj.fit(X_train, y_train.values.ravel())
best_knn = grid_fit.best_estimator_
predictions = (knn.fit(X_train, y_train.values.ravel())).predict(X_test)
best_prediction = best_knn.predict(X_test)
# Predict on dataset which model has not seen before
#print(knn.predict(X_test))

#print(knn.score(X_test, y_test))

print("Best Score:")
print(grid_fit.best_score_)
print("Best Estimator:")
print(best_knn)
print("Best Parameters:")
print(grid_fit.best_params_)
print("Predictions:")
print(predictions)
print("Best Predictions:")
print(best_prediction)
print("Z predictions knn:")
print(knn.predict(Z))
print("Best predictions Grid search:")
print(best_knn.predict(Z))