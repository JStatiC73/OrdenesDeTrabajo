# Generated by Django 3.2.8 on 2021-12-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('IdContacto', models.BigAutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Telefono', models.CharField(max_length=13)),
            ],
        ),
    ]
