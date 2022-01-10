# Generated by Django 3.2.6 on 2022-01-09 14:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0072_alter_addtobag_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtobag',
            name='order_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]