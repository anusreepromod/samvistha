# Generated by Django 3.2.6 on 2021-12-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0030_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='fabric',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='fit',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='sleeve',
            field=models.CharField(max_length=40),
        ),
    ]