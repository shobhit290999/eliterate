# Generated by Django 3.0.5 on 2020-10-08 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20201008_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 8, 2, 42, 10, 890529)),
        ),
    ]
