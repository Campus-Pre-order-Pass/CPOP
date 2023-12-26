# Generated by Django 4.2.3 on 2023-11-16 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0001_initial'),
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateField(verbose_name='訂單日期')),
                ('take_time', models.TimeField(verbose_name='取餐時間')),
                ('total_amount', models.DecimalField(
                    decimal_places=2, max_digits=10, verbose_name='總金額')),
                ('order_status', models.CharField(choices=[('pending', '已下單'), ('processing', '製作中'), (
                    'completed', '完成'), ('canceled', '取消')], default='pending', max_length=50, verbose_name='訂單狀態')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='創建時間')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='order_item', to='Customer.customer', verbose_name='顧客')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='order_item', to='Shop.vendor', verbose_name='供應商')),
            ],
            options={
                'verbose_name': '訂單',
                'verbose_name_plural': '訂單列表',
            },
        ),
    ]
