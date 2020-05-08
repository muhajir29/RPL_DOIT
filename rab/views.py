from django.shortcuts import render

from .forms import Form_Rab

def index(request):
    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'form_rab' : Form_Rab()

        }

    return render(request, 'rab/index.html', context    )


def pengajuan(request):
    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'form_rab' : Form_Rab()

        }

    return render(request, 'rab/pengajuan.html', context    )
