# Generated by Django 4.2.3 on 2023-12-28 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_order_confirmation_hash_orderitem_order_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(verbose_name='訂單日期'),
        ),
        migrations.AlterField(
            model_name='order',
            name='take_time',
            field=models.DateTimeField(verbose_name='取餐時間'),
        ),
    ]
