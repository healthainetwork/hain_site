# Generated by Django 2.0.9 on 2018-11-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=101, verbose_name='Name of User')),
                ('institution', models.CharField(max_length=25, verbose_name='Institution Name')),
                ('degree', models.CharField(blank=True, max_length=10, verbose_name='Highest Degree Held')),
                ('profession', models.CharField(max_length=25, verbose_name='Profession')),
                ('team_role', models.CharField(max_length=30, verbose_name='Role in Team')),
                ('headshot', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(upload_to='')),
                ('company_name', models.CharField(max_length=250, verbose_name='Name of Company')),
                ('company_description', models.CharField(max_length=1000, verbose_name='Company Description')),
                ('company_link', models.URLField()),
                ('posting_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_update', models.CharField(choices=[('C', 'Clincal'), ('B', 'Business and Funding'), ('T', 'Technology')], max_length=1, verbose_name='Update')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('image', models.ImageField(upload_to='')),
                ('article_link', models.URLField()),
            ],
        ),
    ]
