from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from campspot.choices import price_choices, county_choices
from campspot.models import campme


def index(request):

    campspots = campme.objects.all()
    paginator = Paginator(campspots, 3)
    page = request.GET.get('page')
    campspots=paginator.get_page(page)

    context = {
    'campspots': campspots,
    'test': 'Test'
}
    return render(request, 'campspots/campspots.html', context)


# def listing(request):
#     contact_list = Contact.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'list.html', {'page_obj': page_obj})

def campspots(request):
  

    campspots = campme.objects.all()
    paginator = Paginator(campspots, 3)
    page = request.GET.get('page')
    campspots=paginator.get_page(page)

    context = {
    'campspots': campspots,
    'test': 'Test'
}

    return render(request, 'campspots/campspots.html', context)

def campspot(request, campme_id):
  campspot = get_object_or_404(campme, pk=campme_id)

  context = {
    'campspot': campspot
  }

  return render(request, 'campspots/campspot.html', context)


def search(request):
  queryset_list = campme.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # county
  if 'county' in request.GET:
    county = request.GET['county']
    if county:
      queryset_list = queryset_list.filter(county__iexact=county)

  # 
#   if 'bedrooms' in request.GET:
#     bedrooms = request.GET['bedrooms']
#     if bedrooms:
#       queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'county_choices': county_choices,
    # 'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    # 'campspots': queryset_spots,
    'values': request.GET
  }

  return render(request, 'campspots/search.html', context)