from django.contrib import admin

# Register your models here.
from .models import Artikel, Subscriber

admin.site.register(Artikel)
admin.site.register(Subscriber)


