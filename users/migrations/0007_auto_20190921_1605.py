# Generated by Django 2.2.5 on 2019-09-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190921_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='engaggr',
            field=models.FloatField(default=0, max_length='4', verbose_name='Engineering Aggregate (Percentile)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twelveth',
            field=models.FloatField(default=0, max_length=100, verbose_name='12th Percentage'),
        ),
    ]
