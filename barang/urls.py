from django.urls import path

from . import views

urlpatterns = [
    path('', views.barang, name='barang'),
    path('barang/', views.deskripsi_barang, name='deskripsi_barang'),
    path('new_barang/', views.new_barang, name='new_barang'),

]
