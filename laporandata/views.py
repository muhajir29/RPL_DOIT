from django.shortcuts import render

# Create your views here.

from .forms import Form_LaporanDana


def index(request):
    context = {
        'judul':'Laporan Data',
        'subjudul' : 'selamat datang di laporan dana DOIT',

    }

    return render(request, 'laporandata/index.html', context)

def laporandana(request):
    context = {
        'judul':'Laporan Data',
        'subjudul' : 'selamat datang di laporan dana DOIT',
        'form_laporandana' : Form_LaporanDana()
    }

    return render(request, 'laporandata/laporandana.html', context)
