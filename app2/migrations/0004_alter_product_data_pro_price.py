# Generated by Django 4.2.6 on 2023-11-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_alter_cart_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_data',
            name='pro_price',
            field=models.FloatField(null=True),
        ),
    ]
