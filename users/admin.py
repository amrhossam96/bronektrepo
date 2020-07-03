from django.contrib import admin

from .models import Profile, Brocode, Following, Follower, Timeline

admin.site.register(Profile)
admin.site.register(Brocode)
admin.site.register(Following)
admin.site.register(Follower)
admin.site.register(Timeline)