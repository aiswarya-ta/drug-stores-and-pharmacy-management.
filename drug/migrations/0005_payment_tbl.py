# Generated by Django 5.0.1 on 2024-04-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0004_alter_inproducts_tbl_des_alter_outproducts_tbl_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=300)),
                ('numb', models.IntegerField()),
                ('buyer', models.CharField(max_length=30)),
                ('item', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
