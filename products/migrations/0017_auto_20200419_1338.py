# Generated by Django 3.0.5 on 2020-04-19 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20200419_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='shipping',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]