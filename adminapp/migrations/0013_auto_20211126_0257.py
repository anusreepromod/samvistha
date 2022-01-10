# Generated by Django 3.2.6 on 2021-11-26 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='large',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='medium',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='small',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='xlarge',
            field=models.BooleanField(default=False),
        ),
    ]