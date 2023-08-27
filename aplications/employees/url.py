from django.contrib import admin
from django.urls import path
from aplications.employees import views


app_name = "employee_app"
urlpatterns = [
    path("", views.MainView.as_view(),
         name="index"),

    path("listar/",
         views.DisplayAll.as_view(),
         name='listar'),

    path("listar-empleados-admin/",
         views.ListEmployeeAdmin.as_view(),
         name='list_admin'),

    path("pornombre/",
         views.DisplayByName.as_view(),
         name='nombre'),

    path("detalle/<pk>",
         views.EmployeeByDetail.as_view(),
         name='detalle'),

    path("empleadoxdep/<shorname>/",
         views.EmployeeByDepartment.as_view(),
         name='by_department'
         ),
    path("crear-empleado/",
         views.EmployeeFormCreateView.as_view(),
         name="create_employee"),

    path("gracias/", views.Gracias.as_view(), name="gracias"),
    path("actualizar/<pk>/",
         views.EmployeeUpdateView.as_view(),
         name="update_employee"),
    path("eliminar/<pk>/",
         views.EmployeeDeleteView.as_view(),
         name="delete_employee"),
    #path("form/", views.EmployeeFormCreateView.as_view(), name="form"),

]
