import pickle
from model_class import DummyModel  # Import the model class

model = DummyModel()
with open("dummy_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")
