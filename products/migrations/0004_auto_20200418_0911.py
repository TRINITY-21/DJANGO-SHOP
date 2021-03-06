# Generated by Django 3.0.5 on 2020-04-18 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200418_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.IntegerField(max_length=255),
        ),
    ]
