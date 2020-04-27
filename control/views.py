from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'control DOIT',
        'subjudul' : 'Selamat Datang DI Control DOIT',
        'banner' : 'img/banner_doit.jpg',


    }

    return render(request, 'index.html', context)

