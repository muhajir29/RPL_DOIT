
from django.conf.urls import url, include
from django.contrib import admin

from .views import index, loginView, logoutView
from rab.views_transfer import showtransfer, transfer

from rab.views_valtransfer import  valtransfer

urlpatterns = [

    url(r'^login/$', loginView , name = "login"),
    url(r'^logout/$', logoutView, name = "logout"),
    url(r'^admin/', admin.site.urls),

    url(r'^$', showtransfer,  name = "index"),

    url(r'^control/', include('control.urls', namespace = 'control')),
    url(r'^laporandata/', valtransfer  , name = 'valtransfer' ),
    url(r'^rab/', include('rab.urls', namespace = "rab")),
    url(r'^transfer/', transfer , name = 'transfer'),
]




from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
