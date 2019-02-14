from django.contrib import admin
from .models import Barang
# Register your models here.
my_model = [Barang]
admin.site.register(my_model)