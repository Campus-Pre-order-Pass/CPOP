# Generated by Django 4.2.3 on 2023-12-30 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0012_alter_promotion_options_promotion_promotion_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='promotion_type',
            field=models.CharField(choices=[('new_release', '新上市'), ('new_offer', '新優惠'), ('new_discount', '新折扣')], max_length=50, null=True, verbose_name='促銷類型'),
        ),
    ]
