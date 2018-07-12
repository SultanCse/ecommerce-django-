from django.conf.urls import url, include
from .views import show_category_products_list

urlpatterns = [
    url(r'^men/', show_category_products_list, name='men'),
    url(r'^women/', show_category_products_list, name='women'),
    url(r'^baby/', show_category_products_list, name='baby'),
    url(r'^nokia/', show_category_products_list, name='nokia'),
    url(r'^xiaomi/', show_category_products_list, name='xiaomi'),
    url(r'^samsung/', show_category_products_list, name='samsung'),
    url(r'^Televission/', show_category_products_list, name='Televission'),
    url(r'^music/', show_category_products_list, name='music'),
]