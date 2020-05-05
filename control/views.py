from django.shortcuts import render


# import from model
from .models import Post


def index(request):

    posts = Post.objects.all()
    context = {
        'judul' : 'control DOIT',
        'subjudul' : 'Selamat Datang DI Control DOIT',
        'Posts' : posts,


    }

    return render(request, 'index.html', context)

