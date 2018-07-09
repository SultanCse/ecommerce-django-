from django.conf.urls import url
from user import views

urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_fun, name='login'),
    url(r'^logout/$', views.logout_fun, name='logout'),
    # url(r'^login/$', ,name='login'),
]

