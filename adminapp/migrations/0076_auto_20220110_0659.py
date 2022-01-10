# Generated by Django 3.2.6 on 2022-01-10 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0075_addtobag_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='brand_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory_id',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='productid',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category_id',
        ),
        migrations.DeleteModel(
            name='addtobag',
        ),
        migrations.DeleteModel(
            name='brand',
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='discount',
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='stock',
        ),
        migrations.DeleteModel(
            name='subcategory',
        ),
    ]
