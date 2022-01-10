# Generated by Django 3.2.6 on 2021-12-31 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0043_auto_20211231_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=40)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.brand')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=40)),
                ('small', models.BooleanField()),
                ('medium', models.BooleanField()),
                ('large', models.BooleanField()),
                ('xlarge', models.BooleanField()),
                ('unitprice', models.CharField(max_length=40)),
                ('purchaseprice', models.CharField(max_length=40)),
                ('tax', models.CharField(max_length=40)),
                ('fit', models.CharField(max_length=40)),
                ('fabric', models.CharField(max_length=40)),
                ('sleeve', models.CharField(max_length=40)),
                ('pimage1', models.CharField(max_length=50)),
                ('pimage2', models.CharField(max_length=50)),
                ('pimage3', models.CharField(max_length=50)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.category')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.discount')),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=40)),
                ('subcategoryimage', models.CharField(max_length=60)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=40)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.subcategory'),
        ),
    ]