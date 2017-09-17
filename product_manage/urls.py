from django.conf.urls import url
from product_manage import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^register/$', views.register, name="register"),
    url(r'^email_register/$', views.email_register, name="email_register"),
    url(r'^phone_register/$', views.phone_register, name="phone_register"),
    url(r'^login/$', views.do_login, name="login"),
    url(r'^index/$', views.index, name="index"),
    url(r'^product_info/$', views.show_product, name="show_product"),
    url(r'^shopcart/$', views.shopcart, name="shopcart"),
    url(r'cart/view/(?P<product_name>[^/]+)/$', views.add_to_cart, name="add_to_cart"),
    url(r'cart/clean/', views.clean_cart, name="clean_cart"),
]
