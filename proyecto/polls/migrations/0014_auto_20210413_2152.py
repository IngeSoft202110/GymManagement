# Generated by Django 3.1.4 on 2021-04-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20210413_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutina',
            name='clasificacion',
            field=models.CharField(choices=[('Pierna', 'Pierna'), ('Brazo', 'Brazo'), ('Hombro', 'Hombro'), ('Espalda', 'Espalda'), ('Abdomen', 'Abdomen'), ('Cardio', 'Cardio')], default='Pierna', max_length=20),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='dificultad',
            field=models.CharField(choices=[('Principiante', 'Principiante'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado')], default='Principiante', max_length=20),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='sitio',
            field=models.CharField(choices=[('Casa', 'Casa'), ('Gimnasio', 'Gimnasio')], default='Casa', max_length=20),
        ),
    ]