from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# DummyModel class that you pickle and load later
class DummyModel:
    def predict(self, data):
        return [sum(x) for x in data]

# Load the model from the pickle file
with open("dummy_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define InputData class for input validation
class InputData(BaseModel):
    age: int
    height: int
    salary: int

# Root endpoint (handles the GET request to "/")
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI model API!"}

# Prediction endpoint
@app.post("/predict/")
def predict(input_data: InputData):
    data = [[input_data.age, input_data.height, input_data.salary]]
    prediction = model.predict(data)
    return {"prediction": prediction}
