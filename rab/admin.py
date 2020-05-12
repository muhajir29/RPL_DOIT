from django.contrib import admin

# Register your models here.
from .models import Pusat, Sub, Transfer, Rab, ValRab, ValTransfer

admin.site.register(Pusat)
admin.site.register(Sub)
admin.site.register(Transfer)
admin.site.register(Rab)
admin.site.register(ValRab)
admin.site.register(ValTransfer)


