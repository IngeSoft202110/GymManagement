# Generated by Django 3.1.4 on 2021-04-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_ejercicioxrutina'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='sitio',
            field=models.CharField(choices=[('CASA', 'CASA'), ('GIMNASIO', 'GIMNASIO')], default='CASA', max_length=20),
        ),
    ]
