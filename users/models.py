from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

class Brocode(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    brocode_body = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.post_body[:15]+"...."


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    bio = models.CharField(max_length=100, blank=True)
    follows = models.ManyToManyField('self', related_name='follows_list', symmetrical=False, blank=True)
    followers = models.ManyToManyField('self', related_name='followers_list', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
