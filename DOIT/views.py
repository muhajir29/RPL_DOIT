from django.shortcuts import render

def index(request):

    context = {
        'judul' : 'DO IT',
        'subjudul' : 'selamat datang di DOIT (DANA OKE INTIME)',


    }

    return render(request, 'index.html', context)
