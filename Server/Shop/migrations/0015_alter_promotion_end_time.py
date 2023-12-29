# Generated by Django 4.2.3 on 2023-12-30 01:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_promotion_end_time_promotion_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='促銷結束時間'),
            preserve_default=False,
        ),
    ]
