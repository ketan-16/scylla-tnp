# Generated by Django 2.2.5 on 2019-09-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='engaggr',
            field=models.FloatField(default='60', max_length='4'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twelveth',
            field=models.FloatField(max_length='4'),
        ),
    ]
