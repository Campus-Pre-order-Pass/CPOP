# Generated by Django 4.2.3 on 2024-02-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='blacklist_groups',
            field=models.ManyToManyField(help_text='黑名單', related_name='blacklist_users', to='auth.group', verbose_name='黑名單'),
        ),
        migrations.AddField(
            model_name='customer',
            name='whitelist_groups',
            field=models.ManyToManyField(help_text='黑名單', related_name='whitelist_users', to='auth.group', verbose_name='白名單'),
        ),
    ]
