# Generated by Django 3.0.7 on 2020-08-28 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='act',
            field=models.IntegerField(default=0),
        ),
    ]
