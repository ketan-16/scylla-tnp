# Generated by Django 2.2.4 on 2019-09-22 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_grievances'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grievances',
            old_name='author',
            new_name='user',
        ),
    ]
