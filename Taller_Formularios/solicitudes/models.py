from django.db import models

class Solicitud(models.Model):
    class TipoSolicitud(models.TextChoices):
        ACADEMICA = 'AC', 'Académica'
        ADMINISTRATIVA = 'AD', 'Administrativa'
        TECNICA = 'TE', 'Técnica'
        OTRA = 'OT', 'Otra'


    NombreSolicitante = models.CharField(max_length=150)
    DocumentoIdentidad = models.CharField(max_length=50) 
    Correo = models.EmailField()
    Telefono = models.IntegerField()
    TipoSolicitud = models.CharField(
        max_length=20,
        choices=TipoSolicitud.choices, 
        default=TipoSolicitud.OTRA     
    )
    Asunto = models.CharField(max_length=50)
    Descripcion = models.TextField()  
    FechaSolicitud = models.DateField()
    ArchivoAdjunto = models.FileField(upload_to='solicitudes/', null=True, blank=True)

    def __str__(self):
        return f"{self.NombreSolicitante} - {self.TipoSolicitud}"
