from django.conf.urls import url, include
from .views import show_searched_products_list
urlpatterns=[
    url(r'^$', show_searched_products_list, name='search'),
]