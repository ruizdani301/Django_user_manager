from django.test import TestCase

import pytest

from django.urls import reverse
from django.test import RequestFactory
from .models import Employee
from views import DisplayByName

@pytest.mark.django_db
def test_display_by_name_view():
    # Crear algunos empleados para probar
    Employee.objects.create(first_name='John', last_name='Doe', job='1')
    Employee.objects.create(first_name='Jane', last_name='Smith', job='2')

    # Crear una instancia de la vista
    view = DisplayByName()

    # Crear una instancia de RequestFactory
    request_factory = RequestFactory()

    # Crear un request ficticio con parámetros GET
    request = request_factory.get(reverse('display_by_name'), {'nombre': 'John'})

    # Ejecutar el método dispatch de la vista
    response = view.dispatch(request)

    # Verificar que la respuesta sea un código de estado 200
    assert response.status_code == 200

    # Verificar que el contexto de la respuesta contiene la lista de empleados filtrada por nombre
    assert 'object_list' in response.context_data
    object_list = response.context_data['object_list']
    
    # Verificar que la lista de empleados filtrada solo contiene empleados con el nombre 'John'
    assert all(employee.first_name == 'John' for employee in object_list)

