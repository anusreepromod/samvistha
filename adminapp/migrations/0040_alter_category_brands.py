# Generated by Django 3.2.6 on 2021-12-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0039_auto_20211230_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='brands',
            field=models.ManyToManyField(to='adminapp.brand'),
        ),
    ]
