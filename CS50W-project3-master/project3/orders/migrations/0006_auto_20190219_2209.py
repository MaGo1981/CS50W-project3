# Generated by Django 2.0.3 on 2019-02-19 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190219_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='topping1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topping1', to='orders.Topping'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='topping2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topping2', to='orders.Topping'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='topping3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topping3', to='orders.Topping'),
        ),
    ]
