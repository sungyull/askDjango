# Generated by Django 2.0.8 on 2018-09-02 07:05

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180902_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='위도,경도', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
    ]