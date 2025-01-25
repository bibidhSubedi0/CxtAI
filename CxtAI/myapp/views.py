from django.shortcuts import render
from django.http import HttpResponse
# A request handler Basically

def home(request):
    age = None
    height = None
    salary = None
    res = None
    print("Tf am i comming here?")
    if request.method == "POST":
        age = request.POST.get("Age")
        height = request.POST.get("Height")
        salary = request.POST.get("Salary")
        # Simple "processing" logic (for now, just reverse the input)
        res = int(age)*int(height)*int(salary)
    return render(request, 'myapp/home.html', {'your_age': age,'your_height':height,'your_salary':salary,'Final_Analysis':res}) # Render renders the html page to the web page

