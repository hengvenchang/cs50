# Generated by Django 2.0.4 on 2018-05-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaprice',
            name='price',
            field=models.FloatField(),
        ),
    ]