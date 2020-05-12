from django.shortcuts import render

from .forms import Form_Control

# import from model
from .models import Post

def index(request):

    posts = Post.objects.all()
    context = {
        'judul' : 'control DOIT',
        'subjudul' : 'Selamat Datang DI Control DOIT',
        'Posts' : posts,
        'form_control' : Form_Control()


    }

    return render(request, 'control/index.html', context)

