# Generated by Django 4.2.3 on 2023-08-01 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date_created',
            new_name='Date_created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='date_updated',
            new_name='Date_updated',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='Stock',
        ),
    ]
