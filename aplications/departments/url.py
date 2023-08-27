from django.contrib import admin
from django.urls import path
from aplications.departments import views


app_name = "department_app"
urlpatterns = [
    path("nuevo-departamento/", views.NewFormDepartement.as_view(),
         name='custom_form'),
    path("lista-departamento/", views.DepartmentListView.as_view(),
         name='list_department'),

]
