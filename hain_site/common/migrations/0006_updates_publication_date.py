# Generated by Django 2.0.9 on 2018-11-12 22:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20181112_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='publication_date',
            field=models.DateField(default=datetime.date(2018, 11, 12), verbose_name='Date'),
        ),
    ]
