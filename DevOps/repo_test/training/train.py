import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import os

current_path = os.getcwd()
print("current path:", current_path)

subdirectory = "data/iris_data.csv"

# load data
data = pd.read_csv(os.path.join(current_path, subdirectory))

# features and target
X = data.drop("Y", axis=1)
y = data["Y"]

# data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# linear regression
model = SVC()
model.fit(X_train, y_train)

# test 
y_pred = model.predict(X_test)

print(model.score(X_test, y_test))