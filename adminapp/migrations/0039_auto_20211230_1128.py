# Generated by Django 3.2.6 on 2021-12-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0038_auto_20211230_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='brand_id',
        ),
        migrations.AddField(
            model_name='category',
            name='brands',
            field=models.ManyToManyField(related_name='_adminapp_category_brands_+', to='adminapp.category'),
        ),
    ]