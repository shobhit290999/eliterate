# Generated by Django 3.0.5 on 2020-09-09 12:48

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200909_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 9, 4, 48, 22, 658502)),
        ),
        migrations.AlterField(
            model_name='addblog',
            name='post',
            field=ckeditor.fields.RichTextField(max_length=2000),
        ),
    ]