
from django.shortcuts import render, redirect

from .forms import  FormTransfer, FormRab, FormValTransfer

from .models import Rab, Transfer, ValTransfer


def showtransfer(request):
    list_transfer = Transfer.objects.all()
    def sum_data(list_data):
        jumlah = []
        for i in range(len(list_data)):
            jumlah.append(list_data[i][0])
        return sum(jumlah)

    saldo = sum_data(Transfer.objects.all().values_list('jumlah'))
    print(saldo)

    context = {
        'judul': 'Kas data',
        'listtransfer': list_transfer,
        'saldo' : saldo,
    }

    return render(request, 'index.html', context)

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
        return redirect("index")

    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'formtransfer' :FormTransfer,
        }
    return render(request, 'rab/transfer.html', context    )

