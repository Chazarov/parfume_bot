# Generated by Django 5.1.2 on 2024-11-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0006_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunningLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default=' ', verbose_name='Текст бегущей строки')),
            ],
            options={
                'verbose_name_plural': 'Бегущая строка',
            },
        ),
    ]
