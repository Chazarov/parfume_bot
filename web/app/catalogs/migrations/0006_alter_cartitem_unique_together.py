# Generated by Django 5.1.2 on 2024-11-17 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0005_remove_cart_items'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product', 'price_item')},
        ),
    ]
