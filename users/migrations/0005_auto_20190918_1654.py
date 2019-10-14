# Generated by Django 2.2.5 on 2019-09-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190918_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default='John', max_length=20, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='Doe', max_length=20, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tenth',
            field=models.FloatField(default=0.0, max_length=100, verbose_name='10th Percentage'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='engaggr',
            field=models.FloatField(max_length='4', verbose_name='Engineering Aggregate (Percentile)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twelveth',
            field=models.FloatField(max_length=100, verbose_name='12th Percentage'),
        ),
    ]