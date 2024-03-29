# Generated by Django 4.1.2 on 2024-01-09 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_alter_listazelja_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanje',
            fields=[
                ('idStanje', models.IntegerField(primary_key=True, serialize=False)),
                ('nazivStanja', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StatusOglasa',
            fields=[
                ('idStatus', models.IntegerField(primary_key=True, serialize=False)),
                ('nazivStatus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Oglas',
            fields=[
                ('idOglas', models.IntegerField(primary_key=True, serialize=False)),
                ('datumObjave', models.DateField()),
                ('cijena', models.IntegerField()),
                ('idKorisnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('idStanje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stanje')),
                ('idStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.statusoglasa')),
                ('idStrip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.strip')),
            ],
        ),
    ]
