# Generated by Django 2.2.5 on 2019-09-24 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0011_auto_20190924_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='do_list',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 24, 15, 30, 10, 194045, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='do_list',
            table=None,
        ),
    ]
