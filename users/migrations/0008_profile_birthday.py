# Generated by Django 3.0.7 on 2020-06-28 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200628_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(default=datetime.date(1990, 1, 1)),
        ),
    ]
