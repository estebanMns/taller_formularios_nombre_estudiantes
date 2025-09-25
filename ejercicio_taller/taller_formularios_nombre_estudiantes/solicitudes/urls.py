from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('exitosa/', views.solicitud_exitosa, name='solicitud_exitosa'),
]