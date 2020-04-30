from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'crib4tonight/index.html')

def about(request):
    return render(request, 'crib4tonight/about.html')


# from django.shortcuts import render
# from django.http import HttpResponse
# from campspot.choices import price_choices, county_choices

# from campspot.models import campme
# from contacts.models import Contact

# def index(request):
#     # listings = campme.objects.order_by('-list_date').filter(is_published=True)[:6]
#     campspots = campme.objects.order_by('price')[:6]

#     context = {
#         'campspots': campspots,
#         'county_choices': county_choices,
#         # 'bedroom_choices': bedroom_choices,
#         'price_choices': price_choices
#     }

#     return render(request, 'crib4tonight/index.html', context)


# def about(request):
#     # Get all realtors
#     contacts = Contact.objects.order_by('contact_date')

#     # Get MVP
#     mvp_contacts = Contact.objects.all().filter(is_mvp=True)

#     context = {
#         'contacts': contacts,
#         'mvp_contacts': mvp_contacts
#     }

#     return render(request, 'crib4tonight/about.html', context)

