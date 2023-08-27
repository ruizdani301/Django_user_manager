from django import forms

""" Se crea el formulario personalizado"""


class DepartmentForm(forms.Form):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=50)
