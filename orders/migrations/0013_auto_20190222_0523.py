# Generated by Django 2.0.3 on 2019-02-22 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20190222_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='sub1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub1', to='orders.Sub'),
        ),
    ]
