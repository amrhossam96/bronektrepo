from django.urls import path, include
from . import views
from .api.users import urls as apiUrl

urlpatterns = [
    path('',views.index,name='register'),
    path('home',views.home,name='home'),
    path('logout',views.logout_page,name='logout'),
    path('login',views.login_page,name='login'),

]