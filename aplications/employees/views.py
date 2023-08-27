from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView
from aplications.employees.models import Employee
from django.urls import reverse_lazy
from .forms import EmployeForm


class MainView(TemplateView):
    """ start view """
    template_name = 'index.html'


"""
al usar paginator_by el mostrara los x registros q se den
encada pagina y la forma de ver cada pagina seria
http://127.0.0.1:8000/listar/?page=2
"""


class DisplayAll(ListView):
    template_name = 'employee/list_all.html'
    paginate_by = 5
    ordering = 'first_name'

    def get_queryset(self):
        # retorna una lista Quersyset
        parameter = self.request.GET.get('kword', '')
        lista = Employee.objects.filter(first_name__icontains=parameter)
        return lista
# class DisplayByDepartment(ListView):
#   # Lo que esta abajo son atributos de ListView
#     template_name = 'employe/list_by_dep.html'
#     queryset = Employee.objects.filter(department__name='contaduria')

  # Usando parametro en la url se reescribe el metodo
  # get_queryset(self)
  # Sl no tener el queryset se hace necesario agregar el m,odel


class ListEmployeeAdmin(ListView):
    template_name = 'employee/list_employee_admin.html'
    paginate_by = 5
    ordering = 'first_name'
    context_object_name = 'employee'
    model = Employee


"""
  The class DisplayByDepartment is a subclass of ListView that displays a list of employees  filtered by department.
"""


class EmployeeByDetail(DeleteView):
    model = Employee
    template_name = 'employee/employee_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeByDetail, self).get_context_data(**kwargs)
        context['titulo'] = 'EMPLEADO DEL MES'
        return context


class EmployeeByDepartment(ListView):
    # Lo que esta abajo son atributos de ListView
    template_name = 'employee/list_by_department.html'
    context_object_name = 'employee'
    paginate_by = 4

    def get_queryset(self):
        # retorna una lista Quersyset
        # Recibe un parametro en la url llamado shorname
        parameter = self.kwargs['shorname']
        list_employee = Employee.objects.filter(
            department__short_name=parameter)
        return list_employee


class DisplayByName(ListView):
    # Lo que esta abajo son atributos de ListView
    template_name = 'employee/clave.html'

    def get_queryset(self):
        # retorna una lista Quersyset
        parametro = self.request.GET.get('nombre',)
        lista = Employee.objects.filter(first_name=parametro)
        print(lista)
        return lista


"""
  La vista TemplateView solo sirve para mostar un templete o html
  solo usa 1 atributos
  * templete_name

"""


class Gracias(TemplateView):
    template_name = 'employee/gracias.html'


"""
  Crea un formulario para accesar registros en la bd
  siempre debe llevar el atributo
  * fields = () que puede ser una lista o (__all__), estos son
    los  campos del modelo que pueden ser todos o algunos
  * success_url = '.' usado para redireccionar
  * reverse_lazy = se usa para redireccionar urls por nombre de
    url
    video 49
"""


# class EmployeCreateView(CreateView):
#     template_name = "employe/add.html"
#     model = Employee
#     #fields = ['first_name', 'job']
#     fields = ('__all__')
#     #success_url = '.'
#     success_url = reverse_lazy('internas_app:gracias')


"""
   En caso de usar form_valid
   form que crea createview no muestre el campo fullname NO significa que el campo no exista en el form y al momento de instanciarlo puedo acceder a el normalmente

"""


class EmployeeFormCreateView(CreateView):
    template_name = "employee/create_employee.html"
    model = Employee
    form_class = EmployeForm
    # fields = ['first_name', 'job']
    # success_url = '.'
    success_url = reverse_lazy('employee_app:list_admin')

    def form_valid(self, form):
        # logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmployeeFormCreateView, self).form_valid(form)


"""
 Uso de la vista generica UpdateView
 * necesita de un parametro para saber a que registro debe actualizar
 * la url requiere de una <pk>
 * requiere del field []
 * success_url =

"""


"""
  The EmployeeUpdateView class is a view for updating employee information and redirects to a success page after successful update.
"""


class EmployeeUpdateView(UpdateView):
    template_name = "employee/update_employee.html"
    model = Employee
    fields = fields = ['first_name',
                       'last_name',
                       'department',
                       'job',
                       'skills',
                       ]
    # success_url = '.'
    success_url = reverse_lazy('employee_app:list_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmployeeUpdateView, self).form_valid(form)


"""
  Vista generica DeleteView
  requiere:
  * model
  * template_name
  * success_url = 
"""

"""
  The EmployeeDeleteView class is a view for deleting an Employee object and redirects to the
  employee_app:list_admin URL upon successful deletion.
"""


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employee/delete_employee.html"

    # success_url = '.'
    success_url = reverse_lazy('employee_app:list_admin')


"""
  Vista creada para hacer la practica del model.form
  en este caso no usara el fields ya que viene defnido desde el employeForm
  y se renderizara usando el form_class
  * De esta manera podremos editar los campos del formulario de la variable form
    en el html
  
"""


"""
The `EmployeFormCreateView` class is a view for creating a new employee record using a form, with a custom template and success URL.
"""


# class EmployeFormCreateView(CreateView):
#     template_name = "employee/prueba_form.html"
#     model = Employee
#     #fields = ['first_name', 'last_name', 'job',]
#     form_class = EmployeForm
#     # success_url = '.'
#     success_url = reverse_lazy('internas_app:gracias')

#     # def form_valid(self, form):
#     #     # logica del proceso
#     #     empleado = form.save()
#     #     empleado.full_name = empleado.firt_name + ' ' + empleado.last_name
#     #     empleado.save()
#     #     return super(EmployeCreateView, self).form_valid(form)
