from django.shortcuts import render, redirect
from .forms import  FormTransfer, FormRab, FormValTransfer
from .models import Rab, Transfer, ValTransfer

def deletetransfer(request, delete_id):
    Transfer.objects.filter(id = delete_id).delete()
    return redirect('index')


def showtransfer(request):



    list_transfer = Transfer.objects.all()
    def sum_data(list_data):
        jumlah = []
        for i in range(len(list_data)):
            jumlah.append(list_data[i][0])
        return sum(jumlah)
    saldo_pemasukan     = sum_data(Transfer.objects.all().values_list('jumlah'))
    saldo_pengeluaran   = sum_data(Transfer.objects.all().values_list('pengeluaran'))
    list_data = []
    data_saldo = 0
    for data in list_transfer:
        data_saldo      += data.jumlah
        data_saldo      -= data.pengeluaran
        data_masuk      = {}
        data_masuk['id']                = data.id
        data_masuk['pusat']             = data.pusat
        data_masuk['sub']               = data.sub
        data_masuk['tanggal_transfer']  = data.tanggal_transfer
        data_masuk['uraian']            = data.uraian
        data_masuk['jumlah']            = data.jumlah
        data_masuk['pengeluaran']       = data.pengeluaran
        data_masuk['saldo']             = data_saldo
        list_data.append(data_masuk)

    context = {
        'judul'             : 'Kas data',
        'listtransfer'      : list_data,
        'saldo_pemasukan'   : saldo_pemasukan,
        'saldo_pengeluaran' : saldo_pengeluaran,
        'saldo_total'       : data_saldo,

    }

    return render(request, 'index.html', context)

from datetime import datetime

def transfer(request):
    data_trans = Transfer.objects.all()




    data_transfer= FormTransfer(request.POST or None)

    print(data_transfer)

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

