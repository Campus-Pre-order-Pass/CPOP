# Generated by Django 4.2.3 on 2024-01-03 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MenuItem', '0007_menuitem_remaining_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menustatus',
            name='date',
            field=models.DateField(default=datetime.date(2024, 1, 3), verbose_name='日期'),
        ),
    ]
