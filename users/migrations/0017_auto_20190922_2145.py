# Generated by Django 2.2.4 on 2019-09-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_grievances_is_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievances',
            name='is_answered',
            field=models.BooleanField(default=False, verbose_name='Is Answered?:'),
        ),
    ]