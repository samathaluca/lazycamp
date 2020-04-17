from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'crib4tonight/index.html')

def about(request):
    return render(request, 'crib4tonight/about.html')

