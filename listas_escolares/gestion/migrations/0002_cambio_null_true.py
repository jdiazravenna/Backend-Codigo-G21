# Generated by Django 5.1.4 on 2025-01-03 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0001_migracion_inicial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto",
            name="descripcion",
            field=models.TextField(null=True),
        ),
    ]
