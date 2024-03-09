# Generated by Django 4.1.6 on 2023-02-16 16:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_order_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='uniq_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
