# Generated by Django 5.1.2 on 2024-11-16 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductTipe',
            new_name='ProductType',
        ),
    ]
