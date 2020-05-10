
from django.conf.urls import url, include
from django.contrib import admin

from .views import index, loginView, logoutView


urlpatterns = [

    url(r'^login/$', loginView , name = "login"),
    url(r'^logout/$', logoutView, name = "logout"),
    url(r'^$', index,  name = "index"),
    url(r'^admin/', admin.site.urls),
    url(r'^control/', include('control.urls')),
    url(r'^laporandata/', include('laporandata.urls')),
    url(r'^rab/', include('rab.urls')),
    url(r'^transfer/', include('transfer.urls')),


]
