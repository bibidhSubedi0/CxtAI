from django.shortcuts import render

def home(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        # Simple "processing" logic (for now, just reverse the input)
        result = user_input[::-1]
    return render(request, 'myapp/home.html', {'result': result})
