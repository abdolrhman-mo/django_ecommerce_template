# Generated by Django 5.0.3 on 2024-04-12 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_product_no_of_items_product_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
