# Generated by Django 2.0.4 on 2018-05-05 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.ForeignKey(null='false', on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaPrice'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaType'),
        ),
    ]
