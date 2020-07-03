from django.shortcuts import render
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import Brocode, Profile


def index(request):

    context = {}

    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                User.objects.get(email=email)
                error = 'Email Already exits'
                context['error'] = error
                context['form'] = form
                return render(request,'users/registeration.html',context)

            except User.DoesNotExist:

                username    = form.cleaned_data['username']
                first_name  = form.cleaned_data['first_name']
                last_name   = form.cleaned_data['last_name']
                password    = form.cleaned_data['password']
                user        = User(
                    username    = username,
                    email       = email,
                    first_name  = first_name,
                    last_name   = last_name
                )
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect('home')

        else:
            return render(request,'users/registeration.html',{'form':form})

    form = UserRegistrationForm()
    context['form'] = form

    return render(request,'users/registeration.html',context)

def home(request):

    if request.method == "POST":
        post_body = request.POST['post-body']
        post = Brocode(author= request.user, brocode_body = post_body)
        post.save()

    try:
        user = User.objects.get(username=request.user)
    except:
        return redirect('register')
    brocodes = user.profile.brocode_set.all().order_by('-created')[:3]

    context = {"brocodes":brocodes}
    return render(request,'users/index.html',context)

def logout_page(request):
    logout(request)
    return render(request,'users/logout.html',{})


def login_page(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password= password)
        if user:
            login(request, user)
            return redirect('home')

    form = UserLoginForm()
    context = {
        'form':form,
    }
    return render(request,'users/login.html',context)