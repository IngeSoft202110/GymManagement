# Generated by Django 3.1.4 on 2021-05-02 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20210430_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.rutina')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.usuario')),
            ],
        ),
    ]
