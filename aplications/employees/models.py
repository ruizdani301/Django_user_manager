from django.db import models
from aplications.departments.models import Department


class Skill(models.Model):
    skill = models.CharField('skill', max_length=50)

    class Meta:
        db_table = 'habilidad'
        verbose_name_plural = 'habilidad empleado'

    def __str__(self):
        return f'{self.id} {self.skill}'


class Employee(models.Model):

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('apellido', max_length=60)
    full_name = models.CharField('NombreCompleto', max_length=150, blank=True)
    job = models.CharField('ocupaciòn', max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    #Creacion de relacion muchos a muchos
    skills = models.ManyToManyField(Skill)

    class Meta:
        db_table = 'empleado'
        verbose_name = 'empleado'
        verbose_name_plural = 'Empleado de la empresa'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.job} {self.first_name} {self.last_name}'
