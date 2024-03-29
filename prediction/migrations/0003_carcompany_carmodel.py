# Generated by Django 5.0 on 2024-01-23 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_cardetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarCompany',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('car_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prediction.carcompany')),
            ],
        ),
    ]
