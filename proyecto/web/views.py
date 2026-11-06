from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def science(request):
    return render(request, 'science.html')

def about(request):
    return render(request, 'about.html')