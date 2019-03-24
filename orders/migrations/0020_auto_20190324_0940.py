# Generated by Django 2.0.3 on 2019-03-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20190319_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='price',
        ),
        migrations.AddField(
            model_name='food',
            name='priceLarge',
            field=models.FloatField(default=7.95),
        ),
        migrations.AddField(
            model_name='food',
            name='priceSmall',
            field=models.FloatField(default=6.5),
        ),
    ]
