
from django.conf.urls import url, include
from django.contrib import admin

from .views import index, loginView, logoutView
from rab.views_transfer import showtransfer, deletetransfer, transfer

from rab.views_valtransfer import  valtransfer, valtransfer_show, valtransfer_send

urlpatterns = [

    url(r'^login/$', loginView , name = "login"),
    url(r'^logout/$', logoutView, name = "logout"),
    url(r'^admin/', admin.site.urls),

    url(r'^delete/(?P<delete_id>[0-9]+)$',  deletetransfer , name = 'deletetransfer'),
    url(r'^$', showtransfer,  name = "index"),



    url(r'^control/', include('control.urls', namespace = 'control')),
    url(r'^rab/', include('rab.urls', namespace = "rab")),
    url(r'^transfer/', transfer , name = 'transfer'),

    url(r'^laporandata/category/(?P<val_trans_input>[0-9]+)/$', valtransfer_show, name = 'valtransfer_show' ),
    url(r'^laporandata/transfer/(?P<trans_input>[0-9]+)/$', valtransfer_send ),
    url(r'^laporandata/', valtransfer  , name = 'valtransfer' ),

]




from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
