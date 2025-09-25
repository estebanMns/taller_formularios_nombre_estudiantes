from django.db import models

class Solicitud(models.Model):
    """
    Modelo para gestionar las solicitudes.
    """
    TIPO_DE_SOLICITUD = (
        ('ACADEMICA', 'Académica'),
        ('ADMINISTRATIVA', 'Administrativa'),
        ('TECNICA', 'Técnica'),
        ('OTRA', 'Otra'),
    )

    nombre_solicitante = models.CharField(max_length=150, verbose_name="Nombre del Solicitante")
    documento_de_identidad = models.CharField(max_length=50, verbose_name="Documento de Identidad")
    correo_electronico = models.EmailField(verbose_name="Correo Electrónico")
    telefono_de_contacto = models.CharField(max_length=20, verbose_name="Teléfono de Contacto")
    tipo_de_solicitud = models.CharField(max_length=20, choices=TIPO_DE_SOLICITUD, verbose_name="Tipo de Solicitud")
    asunto = models.CharField(max_length=100, verbose_name="Asunto")
    descripcion_detallada = models.TextField(verbose_name="Descripción Detallada")

    def __str__(self):
        return f"Solicitud de {self.nombre_solicitante} - {self.asunto}"

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"