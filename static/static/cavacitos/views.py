from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    return render(request, 'index.html')


def cobro(request):
    return render(request, 'index.html')
