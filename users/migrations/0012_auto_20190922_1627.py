# Generated by Django 2.2.4 on 2019-09-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_grievances_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievances',
            name='company_name',
            field=models.CharField(default='', max_length=30, verbose_name='Company Name:'),
        ),
        migrations.AlterField(
            model_name='grievances',
            name='user_query',
            field=models.TextField(default='Q. ', max_length=20, verbose_name='Question:'),
        ),
    ]
