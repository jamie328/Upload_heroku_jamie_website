# Generated by Django 2.2.5 on 2019-09-30 11:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0009_auto_20190930_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 11, 26, 3, 746960, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bbs_comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 11, 26, 3, 746960, tzinfo=utc)),
        ),
    ]
