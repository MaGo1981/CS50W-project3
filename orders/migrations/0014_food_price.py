# Generated by Django 2.0.3 on 2019-03-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20190222_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.FloatField(default=2.0),
        ),
    ]