from django.http import HttpResponse
from django.shortcuts import render
# importamos la vista necesaria para crear un formulario personalizado
# Q use varias tablas
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import DepartmentForm
from .models import Department
from aplications.employees.models import Employee


class DepartmentListView(ListView):
    model = Department
    template_name = "department/list_department.html"


"""
  The above class is a form view in Django that handles the submission of a form for creating a new department and employee.
"""


class NewFormDepartement(FormView):
    template_name = 'department/custom_form.html'
    form_class = DepartmentForm
    success_url = "/"

    def form_valid(self, form):
        print("se ejecuto correctamente")

        # EXisten dos formas de registar los datos q se
        # traen desde el formulario
        # UNA INSTANCIA
        depa = Department(name=form.cleaned_data['department'],
                          short_name=form.cleaned_data['short_name']
                          )
        depa.save()

        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']

        # Usando el ORM de django es la otra forma
        Employee.objects.create(
            first_name=name,
            last_name=last_name,
            job='1',
            department=depa
        )
        return super(NewFormDepartement, self).form_valid(form)
