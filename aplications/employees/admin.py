from django.contrib import admin

# Register your models here.

from aplications.employees.models import *
# Register your models here.

admin.site.register(Skill)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'department',
        'job',
        'full_name',
    )
    # Agrega el campo de busqueda por el parametro dado en el admin
    search_fields = ('first_name',)
    # list_filter crea una caja para filtar por el parametro
    list_filter = ('job',)
    # filter horizontal, lo use para crear un filtro para el campo de muchos a muchos
    filter_horizontal = ('skills',)

    # Agregar campo extra que no este en el modelo
    # la funcion debe llamarse igual que el campo

    def full_name(self, obj):
        # aqui va el codigo necesario
        return obj.first_name + ' ' + obj.last_name


admin.site.register(Employee, EmployeeAdmin)
