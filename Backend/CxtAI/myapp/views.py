from django.shortcuts import render
from django.http import HttpResponse


import requests

def home(request):
    res = None
    if request.method == "POST":
        age = int(request.POST.get("Age"))
        height = int(request.POST.get("Height"))
        salary = int(request.POST.get("Salary"))

        # Call the FastAPI microservice
        try:
            response = requests.post(
                "http://127.0.0.1:5000/predict/",
                json={"age": age, "height": height, "salary": salary},
            )
            response_data = response.json()
            res = response_data.get("prediction")
        except requests.exceptions.RequestException as e:
            res = f"Error connecting to prediction service: {e}"

    return render(request, 'myapp/home.html', {'Final_Analysis': res})
