from django.shortcuts import render, redirect
from .forms import  FormTransfer, FormRab, FormValTransfer
from .models import Rab, Transfer, ValTransfer, Sub, Pusat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group ,User



def deletetransfer(request, delete_id):
    Transfer.objects.filter(id = delete_id).delete()
    return redirect('index')


def showtransfer(request):
    def sum_data(list_data):
        jumlah = []
        for i in range(len(list_data)):
            jumlah.append(list_data[i][0])
        return sum(jumlah)
    #print(request.user.filter())
    print()
    print(request.user.id, "ini id")
    print(request.user, 'ini usernya')
    for data in request.user.groups.all():
        print(data, 'ini group nya')
    print(Group.objects.get(name= 'provinsi'), ' ini get provinsi')
    print(Group.objects.get(name = 'Jawa_Barat'), 'ini get jawa barat')
    # ini mengambil id dari model sub id agar dapat masuk pada filter
    try:
        id_transfer_sub = Sub.objects.get(nama_sub_id = request.user.id).id
    except:
        id_transfer_pusat = Pusat.objects.get(nama_id = request.user.id).id

    if request.user.id == 1:
        list_transfer = Transfer.objects.all()
        data_pemasukan = sum_data(Transfer.objects.all().values_list('jumlah'))
        data_pengeluaran = sum_data(Transfer.objects.all().values_list('pengeluaran'))
    elif Group.objects.get(name = 'provinsi') in request.user.groups.all():
        list_transfer = Transfer.objects.filter(pusat_id = id_transfer_pusat)
        data_pemasukan = sum_data(Transfer.objects.filter(pusat_id = id_transfer_pusat).values_list('jumlah'))
        data_pengeluaran = sum_data(Transfer.objects.filter(pusat_id = id_transfer_pusat).values_list('pengeluaran'))
        print("masuk sini")
    else:
        list_transfer = Transfer.objects.filter(sub_id = id_transfer_sub)
        data_pemasukan = sum_data(Transfer.objects.filter(sub_id = id_transfer_sub).values_list('jumlah'))
        data_pengeluaran = sum_data(Transfer.objects.filter(sub_id = id_transfer_sub).values_list('pengeluaran'))
        print("masuk jawa barat")
    if request.method == 'POST':
        if request.POST["Logout"] == "Logout":
            logout(request)
        return redirect('login')
    saldo_pemasukan     = data_pemasukan
    saldo_pengeluaran   = data_pengeluaran
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

    template_name = None
    if request.user.is_authenticated():
        template_name = 'index.html'
    else:
        template_name = 'login.html'
    return render(request, template_name , context)



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

