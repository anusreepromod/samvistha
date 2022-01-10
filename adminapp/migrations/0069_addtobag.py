# Generated by Django 3.2.6 on 2022-01-09 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_address'),
        ('adminapp', '0068_delete_addtobag'),
    ]

    operations = [
        migrations.CreateModel(
            name='addtobag',
            fields=[
                ('brand', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
                ('size', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=40)),
                ('order_date', models.CharField(max_length=50)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.product')),
            ],
        ),
    ]