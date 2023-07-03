# Generated by Django 4.2.2 on 2023-06-25 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_kebumen', '0005_destinations_kategori_destinations_suka_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinations',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='destinations',
            name='timeClose',
            field=models.TimeField(default=datetime.time(18, 0)),
        ),
        migrations.AddField(
            model_name='destinations',
            name='timeOpen',
            field=models.TimeField(default=datetime.time(6, 0)),
        ),
    ]