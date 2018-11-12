# Generated by Django 2.0.9 on 2018-11-12 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutmembers',
            options={'verbose_name': 'Team Member', 'verbose_name_plural': 'Team Members'},
        ),
        migrations.AlterModelOptions(
            name='career',
            options={'verbose_name': 'Career', 'verbose_name_plural': 'Careers'},
        ),
        migrations.AlterModelOptions(
            name='updates',
            options={'verbose_name': 'Update', 'verbose_name_plural': 'Updates'},
        ),
        migrations.AlterField(
            model_name='aboutmembers',
            name='degree',
            field=models.CharField(blank=True, max_length=20, verbose_name='Highest Degree Held'),
        ),
        migrations.AlterField(
            model_name='aboutmembers',
            name='institution',
            field=models.CharField(max_length=100, verbose_name='Institution Name'),
        ),
        migrations.AlterField(
            model_name='aboutmembers',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name of User'),
        ),
        migrations.AlterField(
            model_name='aboutmembers',
            name='profession',
            field=models.CharField(max_length=100, verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='aboutmembers',
            name='team_role',
            field=models.CharField(max_length=100, verbose_name='Role in Team'),
        ),
    ]