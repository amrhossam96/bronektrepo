from django.urls import path
from . import views


urlpatterns = [
    path('profile_data',views.response,name='get_response'),
    path('post_brocode',views.post_brocode,name='post_response'),
]