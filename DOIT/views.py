from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from django.contrib.auth import authenticate, login, logout


def index(request):
    context = {
        'judul' : 'DO IT',
        'subjudul' : 'selamat datang di DOIT (DANA OKE INTIME)',
    }
    return render(request, 'index.html', context)




def loginView(request):
    context = {
        "judul" : "DO IT",
        "subjudul" : "SELAMAT DATANG DI DOIT"
    }
    user = None

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
        print(username_login)
        user = authenticate(request, username = username_login, password = password_login)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'login.html', context)



def logoutView(request):
    context = {
            'judul' : "logout",
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)

        return redirect('login')

    return render(request , 'logout.html', context)










