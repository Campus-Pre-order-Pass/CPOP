# Generated by Django 4.2.3 on 2023-11-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_dayofweek_day_alter_dayofweek_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayofweek',
            name='vendor',
        ),
        migrations.AddField(
            model_name='dayofweek',
            name='vendors',
            field=models.ManyToManyField(related_name='days_of_week', to='Shop.vendor', verbose_name='廠商'),
        ),
    ]