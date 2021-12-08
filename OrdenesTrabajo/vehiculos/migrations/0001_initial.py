# Generated by Django 3.2.8 on 2021-12-03 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contactos', '0002_contacto_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('IdVehiculo', models.BigAutoField(primary_key=True, serialize=False)),
                ('Serie', models.CharField(max_length=100)),
                ('Year', models.IntegerField()),
                ('Color', models.CharField(max_length=60)),
                ('Marca', models.CharField(max_length=100)),
                ('Linea', models.CharField(max_length=100)),
                ('IdContacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactos.contacto')),
            ],
        ),
    ]