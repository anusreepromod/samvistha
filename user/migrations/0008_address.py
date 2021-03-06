# Generated by Django 3.2.6 on 2022-01-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_login_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('mobile', models.BigIntegerField()),
                ('addresstype', models.CharField(max_length=30)),
            ],
        ),
    ]
