# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-07 10:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0002_auto_20190407_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.TextField(default='Your Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Tell us something'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]