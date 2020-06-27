from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def index(request):
    if (request.method == "POST"):
        print(request.body)




    return render(request,'users/registeration.html',{})


def home(request):
    return render(request,'users/index.html',{})