# Generated by Django 4.0.5 on 2022-07-15 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1aad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='create_at',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
