from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def campspots(request):
    return render(request, 'campspot/campspots.html')

def campspot(request):
    return render(request, 'campspot/campspot.html')

def search(request):
    return render(request, 'campspot/search.html')

