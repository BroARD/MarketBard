# Generated by Django 5.0.7 on 2024-07-17 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='result',
            field=models.PositiveIntegerField(),
        ),
    ]
