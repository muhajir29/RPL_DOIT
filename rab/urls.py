from django.conf.urls import url

from . import views

from . import views_transfer
from rab import views as views_rab
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pengajuan$', views.pengajuan , name = 'pengajuan'),
    url(r'^delete/(?P<delete_id_pengajuan>[0-9]+)$', views.deletepengajuan, name = 'deletepengajuan'),
    url(r'^transfer$', views_transfer.transfer, name = 'transfer'),
    #url(r'^valtransfer$', views.valtransfer, name = 'valtransfer'),
]


