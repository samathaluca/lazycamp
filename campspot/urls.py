# from django.conf.urls import url, include
# from .views import all_products

# urlpatterns = [
#     url(r'^$', all_products, name='products'),
# ]

from django.urls import path

from campspot import views

urlpatterns = [
    
    path('', views.index, name='camps'),
    path('search/', views.search, name='search'),
    path('campspots/', views.campspots, name='campspots'),
    # path('campspot/<int:campme_id>', views.campspot, name='campspot'),
    path('campspot/<campme_id>', views.campspot, name='campspot'),
    
]