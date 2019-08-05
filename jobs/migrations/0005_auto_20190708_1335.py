# Generated by Django 2.2.2 on 2019-07-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20190708_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='picture1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='job',
            name='picture2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='job',
            name='picture3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='job',
            name='subtitle1',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='job',
            name='subtitle2',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='job',
            name='subtitle3',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
