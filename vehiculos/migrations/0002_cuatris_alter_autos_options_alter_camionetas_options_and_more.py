# Generated by Django 4.2.3 on 2023-08-27 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuatris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Cuatri',
                'verbose_name_plural': 'Cuatris',
                'ordering': ['-marca'],
            },
        ),
        migrations.AlterModelOptions(
            name='autos',
            options={'ordering': ['-marca'], 'verbose_name': 'Auto', 'verbose_name_plural': 'Autos'},
        ),
        migrations.AlterModelOptions(
            name='camionetas',
            options={'ordering': ['-marca'], 'verbose_name': 'Camioneta', 'verbose_name_plural': 'Camionetas'},
        ),
        migrations.AlterModelOptions(
            name='motos',
            options={'ordering': ['-marca'], 'verbose_name': 'Moto', 'verbose_name_plural': 'Motos'},
        ),
    ]