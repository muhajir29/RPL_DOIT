

from django.shortcuts import render, redirect

from .forms import  FormTransfer, FormRab, FormValTransfer

from .models import Rab, Transfer, ValTransfer



def valtransfer(request):
    data_valtransfer= FormValTransfer(request.POST or None, request.FILES)
    list_valtransfer = ValTransfer.objects.all()

    if request.method == "POST":
        print(data_valtransfer)
        if data_valtransfer.is_valid():
            data_valtransfer.save()
            print("tersimpan")
        else:
            print("error")
        return redirect("valtransfer")


    def sum_data(list_data):
        jumlah = []
        for i in range(len(list_data)):
            jumlah.append(list_data[i][0])
        return sum(jumlah)

    saldo = sum_data(list_valtransfer.values_list('harga'))
    print(saldo)
    context ={
        'judul' : 'Validafion data',
        'subjudul' : 'selamat data divalidation',
        'formvaltransfer' : FormValTransfer,
        'listvaltransfer' : list_valtransfer,
        'saldo' :saldo,
        }
    return render(request, 'rab/valtransfer.html', context)



def valtransfer_show(request, val_trans_input):
    fil_valtransfer = ValTransfer.objects.filter(transfer_id = val_trans_input )

    categories = ValTransfer.objects.values('transfer_id').distinct()

    def sum_data(list_data):
        jumlah = []
        for i in range(len(list_data)):
            jumlah.append(list_data[i][0])
        return sum(jumlah)

    saldo = sum_data(fil_valtransfer.values_list('harga'))


    context ={
        'judul' : 'ion data',
        'subjudul' : 'selamat data divalidation',
        'formvaltransfer' : FormValTransfer,
        'filvaltransfer' : fil_valtransfer,
        'categories' : categories,
        'saldo' : saldo,
        'val_input' : val_trans_input,

        }



    return render(request , 'rab/show_valtransfer.html', context)

from datetime import datetime


def valtransfer_send(request, trans_input):
    data_trans = Transfer.objects.get(id = trans_input)

    # untuk mendapatkan total pengeluaran pada id transfer ini
    fil_valtransfer = ValTransfer.objects.filter(transfer_id = trans_input )
    def sum_data(list_data):
        jumlah = []
        for i in range(len(list_data)):
            jumlah.append(list_data[i][0])
        return sum(jumlah)

    saldo = sum_data(fil_valtransfer.values_list('harga'))

    data = Transfer.objects.create(
                pusat_id = data_trans.pusat_id,
                sub_id = data_trans.sub_id,
                tanggal_transfer = datetime.now(),
                uraian = data_trans.uraian,
                jumlah = 0,
                pengeluaran = saldo,

        )
    print(data)
    data.save()


    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'formtransfer' :FormTransfer,
        }

    return redirect('index')










