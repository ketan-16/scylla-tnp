# Generated by Django 2.2.4 on 2019-09-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20190922_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='grievances',
            name='g_username',
            field=models.CharField(default='', max_length=30, verbose_name='UserName:'),
        ),
    ]