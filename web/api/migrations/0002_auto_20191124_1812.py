# Generated by Django 2.2.7 on 2019-11-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trame',
            name='commentaire',
            field=models.CharField(default='', max_length=128, verbose_name='Commentaire'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trame',
            name='content',
            field=models.CharField(max_length=128, verbose_name='Contenu de la trame'),
        ),
    ]