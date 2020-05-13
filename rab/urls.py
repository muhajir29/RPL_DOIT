from django.conf.urls import url

from . import views


from rab import views as views_rab
urlpatterns = [
    url(r'^$', views_rab.showtransfer, name='index'),
    url(r'^pengajuan$', views.pengajuan , name = 'pengajuan'),
    url(r'^transfer$', views.transfer, name = 'transfer'),
    url(r'^valtransfer$', views.valtransfer, name = 'valtransfer'),
]


