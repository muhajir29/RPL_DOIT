from django.shortcuts import render, redirect
from .forms import  FormTransfer, FormRab, FormValTransfer
from .models import Rab, Transfer, ValTransfer, Sub, Pusat
from django.contrib.auth.models import Group ,User



def deletepengajuan(request,delete_id_pengajuan):
    Rab.objects.filter(id=delete_id_pengajuan).delete()
    return redirect('rab:index')


def index(request):

    def sum_data(list_data):
        jumlah = []
        for i in range(len(list_data)):
            jumlah.append(list_data[i][0])
        return sum(jumlah)
    jumlah_pengajuan = sum_data(Rab.objects.all().values_list('jumlah'))

    try:
        id_transfer_sub = Sub.objects.get(nama_sub_id = request.user.id).id
        print(id_transfer_sub)
    except:
        id_transfer_pusat = Pusat.objects.get(nama_id = request.user.id).id
        print(id_transfer_pusat)

    if request.user.id == 1:
        list_rab = Rab.objects.all()
        data_pemasukan = sum_data(Rab.objects.all().values_list('jumlah'))

    elif Group.objects.get(name = 'provinsi') in request.user.groups.all():
        list_rab = Rab.objects.filter(pusat_id = id_transfer_pusat)
        data_pemasukan = sum_data(Rab.objects.filter(pusat_id = id_transfer_pusat).values_list('jumlah'))
        print("masuk sini")
    else:
        list_rab = Rab.objects.filter(sub_id = id_transfer_sub)
        data_pemasukan = sum_data(Rab.objects.filter(sub_id = id_transfer_sub).values_list('jumlah'))
        print("masuk jawa barat")


    print(request.user.id)




#    list_rab = Rab.objects.all()


    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di RAB DOIT',
        'jumlahpengajuan' : jumlah_pengajuan,
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
