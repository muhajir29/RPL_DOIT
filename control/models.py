from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
import sys

from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):

    user_penerima = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    title = models.CharField(max_length = 225)
    body = models.TextField()
    email = models.EmailField(default = 'nama@web.com')
    waktu_posting = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "{}".format(self.title)


from django.db import models
from django.utils.text import slugify
# Create your models here.

