# Generated by Django 3.1.1 on 2021-08-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='User_name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Password',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='student',
            name='User_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]