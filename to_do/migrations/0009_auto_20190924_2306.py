# Generated by Django 2.2.5 on 2019-09-24 15:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0008_auto_20190920_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='do_list',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 24, 15, 6, 10, 483823, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='do_list',
            table='do_list',
        ),
    ]
