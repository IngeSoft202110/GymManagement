# Generated by Django 3.1.4 on 2021-04-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_mensaje_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='usuario',
            field=models.CharField(default='Anonimo', max_length=20),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='sala',
            field=models.IntegerField(default=1),
        ),
    ]
