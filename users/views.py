from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .api.users.serializers import UserModelSerializer
from django.contrib.auth.models import User
import json 


def index(request):
    if (request.method == "POST"):
        data = json.loads(request.body)
        user = User(
            username = data['username'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
        )
        user.set_password(data['password'])
        user.save()



    return render(request,'users/registeration.html',{})


def home(request):
    return render(request,'users/index.html',{})