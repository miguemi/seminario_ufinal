# Generated by Django 4.2.5 on 2023-09-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='nombre',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='nombre',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
