# Generated by Django 5.1.2 on 2024-10-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
