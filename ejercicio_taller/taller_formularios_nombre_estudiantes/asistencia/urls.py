from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_asistencia, name='registro_asistencia'),
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
]