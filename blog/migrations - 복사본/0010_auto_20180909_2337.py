# Generated by Django 2.0.8 on 2018-09-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180909_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=True, to='blog.Post'),
        ),
    ]
