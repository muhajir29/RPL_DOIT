from django.shortcuts import render


from .forms import Form_Transfer
from .forms_provinsi import Form_Transfer_Provinsi
from .forms_kabupaten import Form_Transfer_Kabupaten

def index(request):
    context = {
        'judul': 'TRANSFER',
        'subjudul' : 'Silahkan Masukan Data Transfer',
        'form_transfer': Form_Transfer(),

        }

    return render(request, 'transfer/index.html', context)



def provinsi(request):
    context = {
        'judul': 'TRANSFER',
        'subjudul' : 'Silahkan Masukan Data Transfer',
        'banner' : 'img/banner_doit.jpg',
        'form_transfer': Form_Transfer_Provinsi(),


        }


    return render(request, 'transfer/provinsi.html', context)



def kabupaten(request):
    context = {
        'judul': 'TRANSFER',
        'subjudul' : 'Silahkan Masukan Data Transfer',
        'form_transfer' : Form_Transfer_Kabupaten()

        }

    return render(request, 'transfer/kabupaten.html', context)
