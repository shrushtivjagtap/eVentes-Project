# Generated by Django 3.1 on 2020-08-21 09:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20200821_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventEndTime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 21, 9, 22, 30, 130526, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventStartTime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 21, 9, 22, 30, 130526, tzinfo=utc)),
        ),
    ]
