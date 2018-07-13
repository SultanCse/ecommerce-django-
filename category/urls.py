from django.conf.urls import url, include
from .views import show_category_products_list

urlpatterns = [
    url(r'^(?P<categoryy>[\w-]+)/$', show_category_products_list, name='cat_pro_list'),
]