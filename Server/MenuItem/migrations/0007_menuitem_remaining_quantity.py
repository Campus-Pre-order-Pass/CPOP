# Generated by Django 4.2.3 on 2023-12-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MenuItem', '0006_menustatus_date_alter_menustatus_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='remaining_quantity',
            field=models.PositiveIntegerField(default=20, verbose_name='剩餘數量'),
        ),
    ]