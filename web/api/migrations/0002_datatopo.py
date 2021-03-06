# Generated by Django 3.0 on 2020-01-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTopo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=128, verbose_name='Latitude')),
                ('NorS', models.CharField(max_length=1, verbose_name='N or S')),
                ('longitude', models.CharField(max_length=128, verbose_name='Longitude')),
                ('EorW', models.CharField(max_length=1, verbose_name='E or W')),
                ('depth', models.CharField(max_length=128, verbose_name='Depth')),
                ('antenna_altitude', models.CharField(max_length=128, verbose_name='Altitude Atenna')),
                ('antenna_altitude_metric', models.CharField(max_length=1, verbose_name='Altitude Atenna Metric')),
                ('content', models.CharField(max_length=128, verbose_name='Trame content')),
            ],
            options={
                'verbose_name': 'Trame Topographic',
                'verbose_name_plural': 'Trame Topographics',
            },
        ),
    ]
