# Generated by Django 2.2.5 on 2019-09-24 15:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0012_auto_20190924_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='do_list',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 24, 15, 36, 59, 3319, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='do_list',
            table='do_list',
        ),
    ]
