# Generated by Django 3.0 on 2020-01-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_datatopo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatopo',
            name='antenna_altitude',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Altitude Atenna'),
        ),
        migrations.AlterField(
            model_name='datatopo',
            name='antenna_altitude_metric',
            field=models.CharField(blank=True, default=None, max_length=1, null=True, verbose_name='Altitude Atenna Metric'),
        ),
    ]