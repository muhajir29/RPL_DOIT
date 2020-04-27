from django.shortcuts import render

def index(request):
    context = {
        'judul': 'RAB DOIT',
        'subjudul' : 'Selamat Datang di TRANSFER DOIT',
        'banner' : 'img/banner_doit.jpg',

        }

    return render(request, 'index.html', context)
