from django.conf.urls import url
from products import views

urlpatterns=[
    url(r'^detail/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
]