# Generated by Django 2.2.2 on 2019-07-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190707_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experience1',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='job',
            name='experience2',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='job',
            name='experience3',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
