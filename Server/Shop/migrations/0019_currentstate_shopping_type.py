# Generated by Django 4.2.3 on 2023-12-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0018_promotion_max_purchase_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentstate',
            name='shopping_type',
            field=models.CharField(choices=[('online', '線上購物'), ('physical', '實體購物')], default='online', max_length=10, verbose_name='購物類型'),
        ),
    ]