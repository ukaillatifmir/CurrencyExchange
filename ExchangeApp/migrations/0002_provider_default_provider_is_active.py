# Generated by Django 5.1.1 on 2024-10-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExchangeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='provider',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
