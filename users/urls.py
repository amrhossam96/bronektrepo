from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='register'),
    path('home',views.home,name='home'),
    path('logout',views.logout_page,name='logout'),
    path('login',views.login_page,name='login'),
]