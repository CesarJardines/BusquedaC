# Generated by Django 3.2.5 on 2021-12-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMCE', '0002_auto_20211221_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='voto',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hace',
            name='comentario',
            field=models.TextField(default=''),
        ),
    ]