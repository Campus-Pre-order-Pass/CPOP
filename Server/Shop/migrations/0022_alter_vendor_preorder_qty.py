# Generated by Django 4.2.3 on 2024-01-21 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0021_vendordailymetrics_current_purchase_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='preorder_qty',
            field=models.IntegerField(blank=True, default=20, null=True, verbose_name='預訂數量'),
        ),
    ]
