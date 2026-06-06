import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv("data/student_data.csv")

X = df.drop("G3", axis=1)
y = df["G3"]

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

score = r2_score(y_test, predictions)

print("R2 Score:", score)

pickle.dump(
    model,
    open("models/model.pkl", "wb")
)

print("Model Saved")