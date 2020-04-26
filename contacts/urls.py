from django.urls import path

from crib4tonight import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]