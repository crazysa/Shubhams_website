# Generated by Django 3.2.7 on 2021-09-11 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydata',
            name='phoneno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mydata',
            name='reason',
            field=models.CharField(default='q', max_length=400),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='date',
            field=models.DateField(default=datetime.time(9, 0)),
        ),
    ]