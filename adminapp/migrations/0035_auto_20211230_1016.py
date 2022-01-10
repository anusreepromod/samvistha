# Generated by Django 3.2.6 on 2021-12-30 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0034_auto_20211230_1013'),
    ]

    operations = [
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
            name='category',
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
