from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField

# Create your models here.
class Barang(models.Model) :
    gambar = models.ImageField (upload_to="images")
    nama = models.CharField (max_length=255)
    harga = models.CharField(max_length=255)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama