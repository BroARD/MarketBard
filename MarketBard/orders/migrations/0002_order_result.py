# Generated by Django 5.0.7 on 2024-07-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='result',
            field=models.PositiveIntegerField(default=0),
        ),
    ]