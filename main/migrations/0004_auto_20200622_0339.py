# Generated by Django 3.0.7 on 2020-06-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200622_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.TextField(default='FaceBook'),
        ),
        migrations.AddField(
            model_name='main',
            name='lkdn',
            field=models.TextField(default='LinkdIn'),
        ),
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.TextField(default='setting'),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.TextField(default='Twitter'),
        ),
    ]