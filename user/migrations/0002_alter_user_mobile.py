# Generated by Django 3.2.6 on 2021-09-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
