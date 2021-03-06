# Generated by Django 2.0.9 on 2018-12-24 06:43

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20181224_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seminar',
            name='date_location',
        ),
        migrations.AddField(
            model_name='seminar',
            name='event_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='seminar',
            name='location',
            field=tinymce.models.HTMLField(default='<p>Time:</p><p>Location:</p>', verbose_name='Time & Location'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='term',
            field=models.CharField(choices=[('1808', 'Fall 2018'), ('1901', 'Spring 2019'), ('1906', 'Summer 2019'), ('1908', 'Fall 2019'), ('2001', 'Spring 2020')], max_length=4, verbose_name='Term'),
        ),
    ]
