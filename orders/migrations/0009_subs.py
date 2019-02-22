# Generated by Django 2.0.3 on 2019-02-22 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190220_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('food_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Food')),
                ('size', models.CharField(default='small', max_length=64)),
            ],
            bases=('orders.food',),
        ),
    ]
