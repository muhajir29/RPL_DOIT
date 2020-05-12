from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pengajuan$', views.pengajuan , name = 'pengajuan'),
    url(r'^transfer$', views.transfer, name = 'transfer'),
    url(r'^valtransfer$', views.valtransfer, name = 'valtransfer'),
]


