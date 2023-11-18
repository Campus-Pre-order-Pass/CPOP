# Generated by Django 4.2.3 on 2023-11-16 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_alter_dayofweek_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayofweek',
            name='vendors',
        ),
        migrations.AddField(
            model_name='dayofweek',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='day_of_week', to='Shop.vendor', verbose_name='廠商'),
        ),
    ]
