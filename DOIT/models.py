from django.db import models
from django.utils.text import slugify




from django.db import models
from django.contrib.auth.models import User



class Artikel(models.Model):
    judul       = models.CharField(max_length=255)
    isi         = models.TextField()
    penulis     = models.CharField(max_length=255)
    publish     = models.DateTimeField(auto_now_add = True)
    update      = models.DateTimeField(auto_now = True)
    slug        = models.SlugField(blank=True, editable = False)

    def save(self):
        self.slug = slugify(self.judul)
        super(Artikel, self).save()


    def __str__(self):
        return "{}. {}".format(self.id, self.judul)


from django.db import models
from django.contrib.auth.models import User

class Subscriber(models.Model):
    user_rec = models.ForeignKey(User)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'subscribers'

    def __unicode__(self):
        return u"%s's Subscription Info" % self.user_r
