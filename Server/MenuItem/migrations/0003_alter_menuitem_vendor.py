# Generated by Django 4.2.3 on 2023-11-19 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_alter_dayofweek_day'),
        ('MenuItem', '0002_alter_menuitem_extra_option_requiredoption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='Shop.vendor', verbose_name='菜單'),
        ),
    ]
