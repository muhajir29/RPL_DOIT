from django.shortcuts import render, redirect

from .forms import  FormTransfer, FormRab, FormValTransfer

from .models import Rab, Transfer, ValTransfer


def deletepengajuan(request,delete_id_pengajuan):
    Rab.objects.filter(id=delete_id_pengajuan).delete()
    return redirect('rab:index')


def index(request):
    list_rab = Rab.objects.all()

    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'form_rab' : FormRab(),
        'listrab' : list_rab,
        }
    return render(request, 'rab/index.html', context )

def pengajuan(request):
    data_rab = FormRab(request.POST or None)
    form_rab = FormRab()
    if request.method == "POST":
        print(Rab.objects.all())
        print(request.POST.get('pusat'))
        if data_rab.is_valid():
            data_rab.save()
            print("tersave")
        else:
            data_rab.errors
            print("error")
            print(data_rab.errors)
        #data_rab.save()
        return redirect("rab:index")
    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'form_rab' : FormRab(),
        }
    return render(request, 'rab/pengajuan.html', context    )








###########################################################################################
