from django.conf.urls import url
from search.views import do_search

urlpatterns = [
    url('search', do_search, name='search')
]