
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^control/', include('control.urls')),
    url(r'^laporandata/', include('laporandata.urls')),
    url(r'^rab/', include('rab.urls')),
    url(r'^transfer/', include('transfer.urls')),


]
