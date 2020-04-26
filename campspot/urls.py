# from django.conf.urls import url, include
# from .views import all_products

# urlpatterns = [
#     url(r'^$', all_products, name='products'),
# ]

from django.urls import path

from crib4tonight import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]