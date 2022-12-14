# Generated by Django 3.2.16 on 2022-12-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.FileField(upload_to='customer-images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.FileField(upload_to='product-images'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='photo',
            field=models.FileField(upload_to='shop-images'),
        ),
    ]
