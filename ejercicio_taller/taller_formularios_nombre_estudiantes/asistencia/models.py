from django.db import models

# Create your models here.
class Asistencia(models.Model):

    nomre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    docuemento_identidad = models.CharField(max_length=50, verbose_name="Documento de Identidad")
    correo_electronico = models.EmailField(verbose_name="Correo Electrónico")
    fecha_asistencia = models.DateField(verbose_name="Fecha de Asistencia")
    hora_ingreso = models.TimeField(verbose_name="Hora de Ingreso")
    hora_salida = models.TimeField(verbose_name="Hora de Salida")
    presente = models.BooleanField(default=False, verbose_name="Presente")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")

    def __str__(self):
        return f"Asistencia de {self.nombre_copmpelto} en {self.fecha_asistencia}"
    
    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        