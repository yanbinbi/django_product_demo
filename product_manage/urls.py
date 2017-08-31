from django.conf.urls import url
from product_manage import views

urlpatterns = [
    url(r'^$', views.list, name="list"),
]