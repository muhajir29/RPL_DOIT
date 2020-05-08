from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'judul':'laporan data',
        'subjudul' : 'selamat datang di laporan dana DOIT',
        'banner' : 'img/banner_doit.jpg',

    }


    return render(request, 'laporandata/index.html', context)
