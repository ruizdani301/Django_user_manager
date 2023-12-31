# Generated by Django 4.2.3 on 2023-08-20 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                (
                    "short_name",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Nombre corto"
                    ),
                ),
                ("anulate", models.BooleanField(default=False, verbose_name="Anulado")),
            ],
            options={
                "verbose_name": "Departamento",
                "verbose_name_plural": "Areas de la empresa",
                "db_table": "Department",
                "ordering": ["name"],
                "unique_together": {("name",)},
            },
        ),
    ]
