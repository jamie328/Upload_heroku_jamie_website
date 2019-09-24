# Generated by Django 2.2.5 on 2019-09-24 15:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20190920_0240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('-Create_date',)},
        ),
        migrations.AlterField(
            model_name='articles',
            name='Create_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 24, 15, 6, 10, 483823, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='Birthday',
            field=models.DateField(default=datetime.datetime(2019, 9, 24, 15, 6, 10, 483823, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='articles',
            table='articles',
        ),
        migrations.AlterModelTable(
            name='visit_num',
            table='visit_num',
        ),
    ]
