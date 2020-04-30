from django.urls import path
from campspot import views

urlpatterns = [
    
    # path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('campspots/', views.campspots, name='campspots'),
    # path('campspot/<int:campme_id>', views.campspot, name='campspot'),
    path('campspot/<campme_id>', views.campspot, name='campspot'),
    
]