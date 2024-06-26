# Generated by Django 5.0.3 on 2024-04-14 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_shippingaddress_delivery_instruction'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
