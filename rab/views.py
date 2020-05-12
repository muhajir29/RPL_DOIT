from django.shortcuts import render, redirect

from .forms import  FormTransfer, FormRab, FormValTransfer

from .models import Rab, Transfer, ValTransfer

def index(request):
    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'form_rab' : FormRab()

        }

    return render(request, 'rab/index.html', context    )




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



def transfer(request):
    data_transfer= FormTransfer(request.POST or None)
    print(Transfer.objects.all())
    print(request.POST.get('pusat'))


    if request.method == "POST":
        if data_transfer.is_valid():
            data_transfer.save()
            print("tersave")
        else:
            data_transfer.errors
            print("error")
            print(data_transfer.errors)
        return redirect("rab:index")

    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'formtransfer' :FormTransfer,
        }
    return render(request, 'rab/transfer.html', context    )


def valtransfer(request):
    data_valtransfer= FormValTransfer(request.POST or None, request.FILES)

    if request.method == "POST":
        print(data_valtransfer)
        if data_valtransfer.is_valid():
            data_valtransfer.save()
            print("tersimpan")
        else:
            print("error")

        return redirect("rab:index")

    context ={
        'judul' : 'Validation data',
        'subjudul' : 'selamat data divalidation',
        'formvaltransfer' : FormValTransfer,
        }
    return render(request, 'rab/valtransfer.html', context)

