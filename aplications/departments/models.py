from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField(
        'Nombre corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)

    # Modifica como se visualiza el nombre de la clase en el admin
    # Como ordenar los datos en el admin
    class Meta:
        db_table = 'Department'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name',)

    def __str__(self):
        return f'{self.id} {self.name}'
