# dummy_model.py

class DummyModel:
    def predict(self, data):
        # Dummy prediction logic: just sums the input values
        return [sum(x) for x in data]
