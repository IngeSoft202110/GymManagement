# Generated by Django 3.1.4 on 2021-05-06 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20210502_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ejercicioxrutina')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.usuario')),
            ],
        ),
    ]