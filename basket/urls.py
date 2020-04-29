from django.conf.urls import url
from basket.views import view_basket, add_to_basket, adjust_basket
from django.urls import path

from basket import views

urlpatterns = [
    path('', view_basket, name='view_basket'),
    # path('add/(?P<id>\d+)', add_to_basket, name='add_to_basket'),
    # path('adjust/(?P<id>\d+)', adjust_basket, name='adjust_basket'),
]