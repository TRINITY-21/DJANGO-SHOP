# Generated by Django 3.0.5 on 2020-04-18 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200418_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='shipping',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='delivery',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='town',
            field=models.CharField(max_length=255, verbose_name='Where Do you Stay'),
        ),
    ]
