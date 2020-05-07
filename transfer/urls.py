from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^provinsi$', views.provinsi),
    url(r'^kabupaten$', views.kabupaten),



]
