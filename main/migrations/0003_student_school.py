# Generated by Django 3.1.1 on 2021-08-14 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210814_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.school'),
            preserve_default=False,
        ),
    ]
