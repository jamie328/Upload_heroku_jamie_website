# Generated by Django 2.2.5 on 2019-09-19 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0007_auto_20190919_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='do_list',
            name='event_date',
            field=models.DateField(default=datetime.date(2019, 9, 20)),
        ),
    ]
