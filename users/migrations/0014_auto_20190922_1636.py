# Generated by Django 2.2.4 on 2019-09-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_grievances_g_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievances',
            name='g_username',
            field=models.CharField(default='', max_length=30, verbose_name='Username:'),
        ),
    ]
