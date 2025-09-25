from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
    path('', views.lista_asistencias, name='list'),
    path('nuevo/', views.crear_asistencia, name='create'),
    path('<int:pk>/', views.detalle_asistencia, name='detail'),
]
