# Generated by Django 4.0.3 on 2022-03-12 18:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=100, unique=True)),
                ('category_created', models.DateField(default=datetime.date.today)),
                ('category_updated', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=100, unique=True)),
                ('city_created', models.DateField(default=datetime.date.today)),
                ('city_modifed', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_country', models.CharField(max_length=100, unique=True)),
                ('country_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('country_modifed', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_client', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('client_created', models.DateField(default=datetime.date.today)),
                ('client_updated', models.DateField(default=datetime.date.today)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.country'),
        ),
    ]
