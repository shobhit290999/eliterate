# Generated by Django 3.0.5 on 2020-10-08 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200909_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 8, 2, 24, 16, 404188)),
        ),
    ]
