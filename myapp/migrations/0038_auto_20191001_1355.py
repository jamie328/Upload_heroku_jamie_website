# Generated by Django 2.2.5 on 2019-10-01 05:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_auto_20190930_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Create_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 1, 5, 55, 49, 945872, tzinfo=utc)),
        ),
    ]
