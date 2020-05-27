# Generated by Django 3.0.5 on 2020-04-19 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200419_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='date_posted',
        ),
        migrations.AlterField(
            model_name='delivery',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Products'),
        ),
    ]
