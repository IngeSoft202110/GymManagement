# Generated by Django 3.1.4 on 2021-04-28 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20210413_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]