from django.shortcuts import render

def index(request):

    context = {
        'judul' : 'DO IT',
        'subjudul' : 'selamat datang di DOIT (DANA OKE INTIME)',
        'banner' : 'img/banner_home.png',

    }

    return render(request, 'index.html', context)
