from django.conf.urls import url, include
from cart import views

urlpatterns=[
    url(r'^$', views.cart_home, name='home'),
    url(r'^update/$', views.cart_update, name='update'),
    url(r'^api/cart/$', views.cart_detail_api_view, name='cart-api'),
    url(r'^api/cart/total/$', views.cart_amount_to_total,name='cart-total-api'),
    url(r'^api/cart/siganl/$', views.amount_signal_in_cart_home, name='cart-total-signal-api'),
]