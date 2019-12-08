from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.http import HttpResponse
import datetime
from .forms import *
# Create your views here.


def home(request):
    form = LoginForm()
    return render(request, "index.html", {'form': form})


def cobro(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def login(request):
    username = "not logged in"

    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            name = request.POST.get('nombre')

            if(name != 'Municipio'):
                passw = request.POST.get('contrasena')

                criterion1 = Q(nombre__contains=name)
                criterion2 = Q(contrasena__contains=passw)

                q = Inspector.objects.filter(criterion1 & criterion2)

                if q:
                    return render(request, 'ViewInspector.html')
            else:
                passw = request.POST.get('contrasena')

                criterion1 = Q(nombre__contains=name)
                criterion2 = Q(contrasena__contains=passw)

                q = Inspector.objects.filter(criterion1 & criterion2)

                if q:
                    return render(request, 'Municipio.html')

    else:
        MyLoginForm = LoginForm()
    return render(request, 'index.html', {'form': MyLoginForm})


def agrega(request):
    return render(request, "AddOferente.html")


def edita(request):
    return render(request, "EditOferente.html")
