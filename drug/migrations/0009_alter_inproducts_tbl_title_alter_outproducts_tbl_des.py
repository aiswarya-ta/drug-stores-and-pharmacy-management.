# Generated by Django 5.0.1 on 2024-04-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0008_out_order_tbl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inproducts_tbl',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='outproducts_tbl',
            name='des',
            field=models.TextField(max_length=100),
        ),
    ]
