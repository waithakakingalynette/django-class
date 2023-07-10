# Generated by Django 4.2.3 on 2023-07-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0002_product_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_name', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('number_of_items', models.PositiveIntegerField(default=1)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('description', models.TextField()),
                ('products', models.ManyToManyField(to='inventory.product')),
            ],
        ),
    ]
