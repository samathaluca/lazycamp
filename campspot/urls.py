# from django.conf.urls import url, include
# from .views import all_products

# urlpatterns = [
#     url(r'^$', all_products, name='products'),
# ]

from django.urls import path

from campspot import views

urlpatterns = [
    path('', views.campspot, name='campspot'),
    # path('about/', views.about, name='about'),
    # path('<int:campspot_id>', views.campspot, name='campspot'),
    path('search/', views.search, name='search'),
    path('campspots/', views.campspots, name='campspots'),
]