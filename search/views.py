from django.shortcuts import render
from campspot.models import campme

# Create your views here.
def do_search(request):
    campspots = campme.objects.filter(name__icontains=request.GET['q'])
    return render(request, "campspots/campspots.html", {"campspots": campspots})
