from django.conf.urls import url
from order import views

urlpatterns=[
    url(r'^$', views.order, name='view'),
    url(r'^confirm/$', views.confirm, name='confirm')
]