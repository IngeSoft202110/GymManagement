# Generated by Django 3.1.4 on 2021-05-07 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_historial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
