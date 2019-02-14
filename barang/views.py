from django.shortcuts import render
from .models import Barang
from .forms import PostForm


# Create your views here.
def barang(request) :
    barang = Barang.objects.all()
    return render(request, 'barang/barang.html', {'barang':barang})

def deskripsi_barang(request) :
    barang = Barang.objects.all()
    return render(request, 'barang/detail.html', {'barang':barang})

def new_barang(request) :
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('barang')
    else:
        form = PostForm()
    return render(request, 'barang/new_barang.html', {'form': form})