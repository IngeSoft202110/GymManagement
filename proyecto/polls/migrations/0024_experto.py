# Generated by Django 3.1.4 on 2021-05-20 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_rutina_estatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=264)),
                ('apellido', models.CharField(max_length=264)),
                ('correo', models.EmailField(max_length=254)),
                ('clave', models.CharField(max_length=50)),
            ],
        ),
    ]
