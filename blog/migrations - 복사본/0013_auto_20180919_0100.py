# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 16:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180919_0052 - 복사본'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
