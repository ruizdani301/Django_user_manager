# Generated by Django 4.2.3 on 2023-08-20 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skill",
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
                ("skill", models.CharField(max_length=50, verbose_name="skill")),
            ],
            options={
                "verbose_name": "habilidad empleado",
                "db_table": "habilidad",
            },
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("first_name", models.CharField(max_length=60, verbose_name="Nombre")),
                ("last_name", models.CharField(max_length=60, verbose_name="apellido")),
                (
                    "job",
                    models.CharField(
                        choices=[
                            ("0", "CONTADOR"),
                            ("1", "ADMINISTRADOR"),
                            ("2", "ECONOMISTA"),
                            ("3", "OTRO"),
                        ],
                        max_length=1,
                        verbose_name="ocupaciòn",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(blank=True, null=True, upload_to="empleado"),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="departments.department",
                    ),
                ),
                ("skills", models.ManyToManyField(to="employees.skill")),
            ],
            options={
                "verbose_name": "empleado",
                "verbose_name_plural": "Empleado de la empresa",
                "db_table": "empleado",
                "ordering": ["first_name", "last_name"],
            },
        ),
    ]
