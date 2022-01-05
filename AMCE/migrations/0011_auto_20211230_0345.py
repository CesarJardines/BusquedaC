# Generated by Django 3.2.9 on 2021-12-30 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AMCE', '0010_merge_0006_usertype_0009_pertenecer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id_actividad', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.TextField()),
                ('hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('pasoMG', models.FloatField(blank=True, default=None, null=True)),
                ('voto', models.IntegerField(default=0)),
                ('id_tema', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='AMCE.temas')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Hace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(default='')),
                ('id_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMCE.actividad')),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMCE.equipos')),
                ('id_tema', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='AMCE.temas')),
            ],
        ),
    ]
