# Generated by Django 3.1.4 on 2021-04-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_rutina_sitio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejercicio',
            name='peso',
            field=models.IntegerField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='repeticiones',
            field=models.IntegerField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='rutina',
            name='series',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]
