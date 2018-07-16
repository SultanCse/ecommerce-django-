from django.conf.urls import url
from order import views

urlpatterns=[
    url(r'^$', views.order, name='view'),
    url(r'^confirm/$', views.confirm, name='confirm'),
    url(r'^order/$', views.admin_order, name='order'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]