# Generated by Django 3.2.16 on 2022-12-15 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_products_shop_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.shop'),
        ),
    ]
