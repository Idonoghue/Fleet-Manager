# Generated by Django 2.0.1 on 2018-06-07 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20180527_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartgroup',
            name='group_color',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='datacollection',
            name='name',
            field=models.CharField(default='2018-06-06 19:07:24', max_length=30),
        ),
    ]
