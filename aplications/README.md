al no tener el manage.py en esta carpeta se crea las aplixaciones con este comando.
django-admin startapp employees

# se puede crear un editor de texto desde

Como una app de tercero
https://pypi.org/project/django-ckeditor-5/

- En las views.py Estan la explicacion del uso de las direfrentes clases genericas y sus usos.

* Con esta variable se da un nombre a el conjunto de urls
  app_name = "employe_app"

* reverse_lazy = se usa para redireccionar urls por nombre de  
   url
  En este caso recibe 2 parametros
  - El nombre del conjunto de urls app_name
  - El nombre de la url

employee/form.py :
Se explica como crear un formulario con los campos del modelo y como validar los campos
usando el metodo def clear_nombreCampo()
https://docs.djangoproject.com/en/4.2/ref/forms/widgets/

# Widgets:

    es un diccionario,  Se usan para personalizar los formularios
    * https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
    * https://rutan-medellin.udemy.com/course/curso-profesional-de-programacion-web-con-python-y-django/learn/lecture/17022628#overview

departments/forms:

Se explica como crear un formulario personalizado, usando campos de 2 tablas distintas
en este caso NO usa models.forms SINO forms.Forms
Se crea la vista
