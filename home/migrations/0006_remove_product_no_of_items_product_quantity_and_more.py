# Generated by Django 5.0.3 on 2024-04-12 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_orderitem_date_canceled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='no_of_items',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='ImportProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_imported', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]