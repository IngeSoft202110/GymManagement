# Generated by Django 3.1.4 on 2021-04-08 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210408_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='dificultad',
            field=models.CharField(choices=[('PRINCIPIANTE', 'PRINCIPIANTE'), ('INTERMEDIO', 'INTERMEDIO'), ('AVANZADO', 'AVANZADO')], default='PRINCIPIANTE', max_length=20),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]