# Generated by Django 3.0.7 on 2020-09-02 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_manager_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='ip',
            field=models.TextField(default=''),
        ),
    ]
