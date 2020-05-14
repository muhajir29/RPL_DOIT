from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.utils.text import slugify

class Pusat(models.Model):

    nama = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return "{}.{}".format(self.id, self.nama)

class Sub(models.Model):
    pusat = models.ManyToManyField(Pusat, through = "Transfer")
    nama_sub = models.OneToOneField(User , on_delete = models.CASCADE)
    email = models.EmailField()
    def __str__(self):
        return "{}.{}".format(self.id, self.nama_sub)

class Transfer(models.Model):
    pusat   = models.ForeignKey(Pusat, on_delete = models.CASCADE)
    sub     = models.ForeignKey(Sub, on_delete = models.CASCADE)
    tanggal_transfer = models.DateTimeField(auto_now_add = True)
    uraian = models.CharField(max_length = 100)
    jumlah = models.FloatField(default = 0 )
    pengeluaran = models.FloatField(default = 0)

    def __str__(self):
        return "{}-{}:{}".format( self.pusat, self.sub, self.uraian)


class ValTransfer(models.Model):

    transfer        = models.ForeignKey(Transfer, on_delete = models.CASCADE)
    uraian          = models.CharField(max_length = 40)
    harga           = models.FloatField()
    bukti_item      = models.ImageField( default = 'default.jpg' ,upload_to = 'gambar/bukti_item' )
    bukti_transfer  = models.ImageField(default = 'default.jpg', upload_to = 'gambar/bukti_transfer' )
    slug            = models.SlugField(blank = True, editable = False)

    def save(self):
        self.slug =  slugify(self.transfer_id)
        super(ValTransfer, self).save()

    def __str__(self):
        return "{}".format(self.transfer)

class Rab(models.Model):
    pusat = models.ForeignKey(Pusat, on_delete= models.CASCADE)
    sub = models.ForeignKey(Sub, on_delete = models.CASCADE)
    tanggal = models.DateTimeField(auto_now_add = True)
    nama_kegiatan = models.CharField(max_length = 100)
    deskripsi = models.CharField(max_length = 200)
    tujuan = models.CharField(max_length = 100)
    jumlah = models.FloatField()
    proposal = models.FileField(default = 'default.pdf', upload_to = 'file')

    def __str__(self):
        return "{}-{}:{}".format(self.pusat, self.sub, self.nama_kegiatan)

class ValRab(models.Model):
    rab = models.ForeignKey(Rab, on_delete = models.CASCADE)
    uraian = models.CharField(max_length = 40)
    harga = models.FloatField()
    bukti_item = models.ImageField(default = 'default.jpg', upload_to = 'gambar/bukti_item')
    bukti_transfer = models.ImageField(default = 'default.jpg', upload_to = 'gambar/bukti_transfer')

    def __str__(self):
        return "{}.{}".format(self.rab, self.uraian)













