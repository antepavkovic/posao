# Generated by Django 3.1.5 on 2021-01-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210126_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='telefon2',
            new_name='telefon',
        ),
        migrations.AddField(
            model_name='main',
            name='ime_proizvoda',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='main',
            name='kategorija_proizvoda',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
