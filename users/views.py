from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'users/registeration.html',{})


def home(request):
    return render(request,'users/index.html',{})