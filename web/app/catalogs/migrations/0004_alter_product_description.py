# Generated by Django 5.1.2 on 2024-11-16 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0003_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
