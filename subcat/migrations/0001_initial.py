# Generated by Django 3.0.7 on 2020-07-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('catname', models.CharField(max_length=200)),
                ('catid', models.CharField(max_length=200)),
            ],
        ),
    ]