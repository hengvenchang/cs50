# Generated by Django 2.0.4 on 2018-05-05 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_pizza_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzaname',
            name='type',
            field=models.ForeignKey(null='false', on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaType'),
        ),
    ]
