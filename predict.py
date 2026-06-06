import pickle

model = pickle.load(
    open("models/model.pkl", "rb")
)

print("Model Loaded Successfully")
