# Generated by Django 4.2.6 on 2023-11-19 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='product_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=255, null=True)),
                ('pro_price', models.IntegerField(null=True)),
                ('pro_description', models.CharField(max_length=300, null=True)),
                ('XS', models.BooleanField(default=False)),
                ('S', models.BooleanField(default=False)),
                ('M', models.BooleanField(default=False)),
                ('L', models.BooleanField(default=False)),
                ('XL', models.BooleanField(default=False)),
                ('pro_image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='user_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_birth', models.DateField(null=True)),
                ('user_address', models.CharField(max_length=255, null=True)),
                ('user_number', models.IntegerField(null=True)),
                ('user_gender', models.CharField(max_length=250, null=True)),
                ('user_district', models.CharField(max_length=250, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(through='app2.cart_item', to='app2.product_data')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart_item',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.cartmodel'),
        ),
        migrations.AddField(
            model_name='cart_item',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.product_data'),
        ),
    ]