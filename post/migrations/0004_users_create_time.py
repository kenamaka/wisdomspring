# Generated by Django 3.1.1 on 2021-01-11 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210111_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
