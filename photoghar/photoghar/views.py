# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! I'm home.")
    return render(request, 'home.html')

def aboutpage(request):
    # return HttpResponse("My About page.")
    return render(request, 'about.html')

