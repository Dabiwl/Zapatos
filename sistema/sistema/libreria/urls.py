from django.urls import include, path
from . import views
from .views import login_view, register_view
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.contrib.staticfiles.urls import static

from .views import realizar_venta




urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('paginas/crearH', views.crearH, name='crearH'),
    path('paginas/editarH', views.editarH, name='editarH'),
    path('paginas', views.paginas, name='paginas'),
    path('venta/', views.realizar_venta, name='realizar_venta'),
    path('admin-page/', views.vista_admin, name='admin_page'),
    path('add-employee/', views.AddEmployeeView.as_view(), name='add_employee'),
    path('employee-list/', views.EmployeeListView.as_view(), name='employee_list'),  # Aquí defines la URL 'employee_list'

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)