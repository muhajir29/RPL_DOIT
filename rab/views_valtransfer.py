

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
        'judul' : 'Validafsation data',
        'subjudul' : 'selamat data divalidation',
        'formvaltransfer' : FormValTransfer,
        'listvaltransfer' : list_valtransfer,
        'saldo' :saldo,
        }
    return render(request, 'rab/valtransfer.html', context)


