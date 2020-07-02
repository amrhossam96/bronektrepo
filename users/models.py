from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime

class Brocode(models.Model):
    author       = models.ForeignKey(User, on_delete=models.CASCADE)
    brocode_body = models.TextField(blank=False)
    created      = models.DateTimeField(auto_now_add=True)
    likes        = models.IntegerField(default=0)

    def __str__(self):
        return self.brocode_body





class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete= models.CASCADE)
    display_name    = models.CharField(max_length=50, null=True, blank=True, default= "")
    bio             = models.CharField(max_length=100, blank=True)
    email           = models.EmailField(max_length=120, default='')
    birthday        = models.DateTimeField(default= datetime.date(1990,1,1))

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile = Profile(user=instance)
        profile.email = profile.user.email
        profile.display_name = profile.user.first_name
        profile.save()


class Following(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    follows  = models.ManyToManyField(Profile, related_name='follows_list')

    def __str__(self):
        return self.profile.display_name +" Follows"


class Follower(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    followers  = models.ManyToManyField(Profile, related_name='followers_list')

    def __str__(self):
        return self.profile.display_name +" Followers List"