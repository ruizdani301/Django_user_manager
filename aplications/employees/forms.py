from django import forms
from .models import Employee


class EmployeForm(forms.ModelForm):
    """Form definition for employe."""
    print("********************")

    class Meta:
        """Meta definition for employeform."""

        model = Employee
        fields = ('first_name',
                  'last_name',
                  'job',
                  'department',
                  'avatar',
                  'skills',)

        """ Widgets: es un diccionario,  Se usan para personalizar los formularios
             https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
             https://rutan-medellin.udemy.com/course/curso-profesional-de-programacion-web-con-python-y-django/learn/lecture/17022628#overview
        """
        widgets = {'skills': forms.CheckboxSelectMultiple(
            # datos de personalizacion opcionales
            # attrs={
            #     'placeholder': 'nombre solo letras'
            # }
        )
        }

    """ metodo q se reescribe para validar los campos de un formulario
        https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
    """

    # def clean_first_name(self):
    #     # Se recupera la info que viene en el formulario
    #     # en este caso validare el nombre
    #     nombre = self.cleaned_data['first_name']
    #     if nombre.isalnum():
    #         print(nombre)
    #         raise forms.ValidationError('Deben ser letras no numeros')
    #     return nombre
