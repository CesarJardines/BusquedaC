# Generated by Django 3.2.5 on 2021-11-23 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AMCE', '0008_auto_20211123_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pertenecer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AMCE.equipos')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
