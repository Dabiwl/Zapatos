from django import forms
from .models import Libro, Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields= '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class VentaForm(forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), required=True)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'position', 'department', 'hire_date']