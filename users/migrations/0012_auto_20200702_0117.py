# Generated by Django 3.0.7 on 2020-07-01 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_followers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Followers',
            new_name='Follower',
        ),
    ]