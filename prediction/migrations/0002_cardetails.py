# Generated by Django 5.0 on 2024-01-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]
