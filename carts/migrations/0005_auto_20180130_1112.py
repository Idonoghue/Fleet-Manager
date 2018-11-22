# Generated by Django 2.0.1 on 2018-01-30 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20180123_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='data_set',
        ),
        migrations.AddField(
            model_name='dataset',
            name='cart',
            field=models.ForeignKey(default=99, on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
            preserve_default=False,
        ),
    ]