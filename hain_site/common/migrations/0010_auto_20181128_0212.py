# Generated by Django 2.0.9 on 2018-11-28 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_aboutmembers_team_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmembers',
            name='team_department',
            field=models.CharField(blank=True, max_length=100, verbose_name='Team Department'),
        ),
    ]
