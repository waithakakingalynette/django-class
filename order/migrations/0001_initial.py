# Generated by Django 4.2.3 on 2023-07-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=32, unique=True)),
                ('customer_name', models.CharField(max_length=32)),
                ('customer_email', models.EmailField(max_length=255)),
                ('customer_phone_number', models.CharField(max_length=15)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], max_length=16)),
                ('delivery', models.ManyToManyField(to='delivery.delivery')),
            ],
        ),
    ]
