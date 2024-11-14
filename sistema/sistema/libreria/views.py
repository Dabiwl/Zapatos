from django.shortcuts import render, redirect

from django.http import HttpResponse, FileResponse
from .models import Libro, Horario, Employee
from .forms import LibroForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, VentaForm, EmployeeForm 


from .utils import crear_pdf_factura

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros}) 

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario}) 

def editar(request, id):
    libro=Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario}) 

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'paginas/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UserRegisterForm()
    return render(request, 'paginas/register.html', {'form': form})

def paginas(request):
    paginas = Horario.objects.all()
    return render(request, 'paginas/nosotros.html', {'paginas': paginas}) 

def crearH(request):
    return render(request, 'paginas/crearH.html')

def editarH(request):
    return render(request, 'paginas/editarH.html')

def realizar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            libro = form.cleaned_data['libro']  # Obtiene el libro seleccionado
            pdf_buffer = crear_pdf_factura(libro)  # Genera el PDF de la factura

            # Elimina el libro de la base de datos como parte de la compra
            libro.delete()

            # Crear una respuesta HTTP para descargar el PDF
            return FileResponse(pdf_buffer, as_attachment=True, filename=f"Factura_{libro.titulo}.pdf")

    else:
        form = VentaForm()

    return render(request, 'venta_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def vista_admin(request):
    return render(request, 'admin_page.html')

class AddEmployeeView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'add_employee.html'
    success_url = reverse_lazy('employee_list')

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'